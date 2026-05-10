/* ============================================
   DLC CORE LAYER
   Centralized management for DLC modules and synergies
   ============================================ */

const DlcCore = {
    SUPPORTED_DLCS: {
        'dlc_giustizia_magistratura': {
            name: 'Le Toghe',
            description: 'Sistema giudiziario, magistratura e inchieste.',
            init: () => { if (typeof Judiciary !== 'undefined') Judiciary.init(); }
        },
        'dlc_stampa_media': {
            name: 'La Stampa',
            description: 'Giornalisti, testate e conferenze stampa.',
            init: () => { if (typeof Press !== 'undefined') Press.init(); }
        },
        'dlc_politica_estera': {
            name: 'Diplomazia',
            description: 'Relazioni internazionali e missioni estere.',
            init: () => { if (typeof Diplomacy !== 'undefined') Diplomacy.init(); }
        },
        'il_vecchio_mondo_expansion': {
            name: 'Il Vecchio Mondo',
            description: 'Espansione europea (Spagna, Portogallo, Benelux, Svizzera).',
            init: () => { /* Logic handled in Nations/Map modules */ }
        }
    },

    init() {
        this.ensureBaseState();
        
        const activeDlcs = (Game.state.flags && Game.state.flags.activeDlc) || [];
        console.log('DlcCore: Initializing active DLCs...', activeDlcs);

        activeDlcs.forEach(dlcId => {
            const config = this.SUPPORTED_DLCS[dlcId];
            if (config && typeof config.init === 'function') {
                console.log(`DlcCore: Starting module ${dlcId}`);
                config.init();
            }
        });

        Game.on('new-day', () => {
            this.onNewDay();
        });
    },

    ensureBaseState() {
        if (!Game.state.flags) Game.state.flags = {};
        if (!Game.state.dlcFlags) Game.state.dlcFlags = {};

        // Ensure state for legacy systems if needed
        if (!Game.state.justiceSystem) {
            Game.state.justiceSystem = { integrity: 50, corruptionRisk: 0, justiceCorruption: 0, lastBaseEventDay: -99 };
        }
        if (!Game.state.media) {
            Game.state.media = { channels: 0, impact: 0, trust: 0, mediaImpact: 0 };
        }
    },

    isDlcActive(id) {
        const active = (Game.state.flags && Array.isArray(Game.state.flags.activeDlc)) ? Game.state.flags.activeDlc : [];
        return active.includes(id);
    },

    onNewDay() {
        this.processSynergies();
        this.runLegacyLayers();
    },

    processSynergies() {
        const active = (Game.state.flags && Game.state.flags.activeDlc) || [];
        
        // Example Synergy: Press + Judiciary
        if (active.includes('dlc_giustizia_magistratura') && active.includes('dlc_stampa_media')) {
            if (Math.random() < 0.1) {
                Game.addWorkNotif('Sinergia DLC', 'La stampa segue con particolare attenzione le tue vicende giudiziarie.', `Giorno ${Game.state.day}`);
            }
        }
    },

    // Maintain compatibility with existing logic in runActiveDlcLayers
    runLegacyLayers() {
        const mafiaRank = Math.round(((Game.state.mafia && Game.state.mafia.rispettoCriminale) || 0) / 10);
        
        if (this.isDlcActive('dlc_giustizia_magistratura')) {
            Game.state.justiceSystem.corruptionRisk = Math.min(100, Game.state.justiceSystem.corruptionRisk + Math.max(0, mafiaRank - 2));
            const riskTrial = Math.max(0, 100 - Game.state.justiceSystem.integrity) * mafiaRank;
            Game.state.justiceSystem.riskTrial = riskTrial;
        }

        if (this.isDlcActive('dlc_stampa_media')) {
            const followers = (Game.state.social && Game.state.social.followers) || 0;
            Game.state.media.mediaImpact = followers * 0.05;
        }
    }
};

if (typeof window !== 'undefined') window.DlcCore = DlcCore;
