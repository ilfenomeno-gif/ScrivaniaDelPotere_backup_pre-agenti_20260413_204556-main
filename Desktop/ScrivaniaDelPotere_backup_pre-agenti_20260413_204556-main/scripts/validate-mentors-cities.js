const fs = require('fs');
const path = require('path');

// Load mentor data
const mentorsData = JSON.parse(fs.readFileSync('./data/mentors-parties.json', 'utf8'));

// Nations and ideologies
const nations = ['italy', 'france', 'germany', 'uk', 'spain', 'portugal', 'benelux', 'switzerland'];
const ideologyMap = {
  'radical_left': 'sinistra_radicale',
  'left': 'sinistra',
  'center_left': 'centro_sinistra',
  'center': 'centro',
  'center_right': 'centro_destra',
  'right': 'destra',
  'radical_right': 'destra_radicale'
};

console.log('🔍 VALIDAZIONE MENTORI - Tutti gli stati e ideologie\n');

let totalTests = 0;
let passed = 0;
let failed = 0;
const failureLog = [];

for (const nation of nations) {
  const nationData = mentorsData[nation];
  if (!nationData || !nationData.mentors) {
    console.log(`❌ ${nation.toUpperCase()}: Data missing`);
    failed += 7;
    totalTests += 7;
    continue;
  }

  const mentorsInNation = nationData.mentors;
  
  for (const [engIdeology, itIdeology] of Object.entries(ideologyMap)) {
    totalTests++;
    
    // Find mentors with this ideology
    const mentorsForIdeology = mentorsInNation.filter(m => m.ideology === itIdeology);
    
    if (mentorsForIdeology.length === 0) {
      failed++;
      failureLog.push(`${nation}/${engIdeology}: NO MENTORS`);
    } else {
      // Check if all have bonus text  
        const allHaveBonus = mentorsForIdeology.every(m => (m.bonusText || m.bonus || (m.effects && Object.keys(m.effects).length > 0)));
      if (!allHaveBonus) {
        failed++;
        failureLog.push(`${nation}/${engIdeology}: Missing bonus text in some mentors`);
      } else {
        passed++;
      }
    }
  }
}

// Now check cities
console.log('\n🏙️  VALIDAZIONE CITTÀ - Tutti gli stati\n');

let citiesOk = 0;
let citiesFailed = 0;

for (const nation of nations) {
  const cityFile = `./data/cities_${nation}.json`;
  try {
    const citiesData = JSON.parse(fs.readFileSync(cityFile, 'utf8'));
    const cityCount = Object.keys(citiesData).length;
    const status = cityCount > 0 ? '✅' : '❌';
    console.log(`${status} ${nation.toUpperCase().padEnd(15)} - ${cityCount} città`);
    
    if (cityCount > 0) {
      citiesOk++;
    } else {
      citiesFailed++;
      failureLog.push(`${nation}: NO CITIES`);
    }
  } catch (e) {
    console.log(`❌ ${nation.toUpperCase().padEnd(15)} - FILE NOT FOUND`);
    citiesFailed++;
    failureLog.push(`${nation}: File missing`);
  }
}

// Summary
console.log('\n' + '='.repeat(60));
console.log('📊 RAPPORTO FINALE');
console.log('='.repeat(60));
console.log(`\n✅ MENTORI:`);
console.log(`   Total combinations tested: ${totalTests}`);
console.log(`   Passed: ${passed}/${totalTests}`);
console.log(`   Failed: ${failed}/${totalTests}`);
console.log(`   Pass rate: ${Math.round((passed/totalTests)*100)}%`);

console.log(`\n✅ CITTÀ:`);
console.log(`   Nations OK: ${citiesOk}/8`);
console.log(`   Nations FAILED: ${citiesFailed}/8`);

if (failureLog.length > 0) {
  console.log(`\n⚠️  PROBLEMI RILEVATI:`);
  failureLog.forEach(f => console.log(`   - ${f}`));
} else {
  console.log(`\n✅ NESSUN PROBLEMA! Tutti gli stati e ideologie sono OK`);
}
