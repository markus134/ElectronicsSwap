<template>
  <div class="flex flex-col background">
    <Navbar />
    <div class="flex-grow flex items-center justify-center mt-32 text-2xl">
      <div class="bg-white p-8 rounded shadow-2xl w-2/4 h-9/10 mb-8">
        <h1 class="text-3xl font-semibold mb-4">Usaldusväärsuse süsteem</h1>
        <div class="leading-relaxed">
          <p>
            Me ElectronicsSwapis mõistame, et usaldus ja usaldusväärsus mängivad elektroonika laenutamise ja laenutamise maailmas keskset rolli.
          </p>
          <p>
            <div class="text-white">a</div>
          </p>
          <p>
            Meie usaldusväärsuse hindamissüsteem on loodud selleks, et hinnata kasutajate usaldusväärsust ja anda meie kogukonnale kindlustunnet oma tehingute suhtes. See süsteem liigitab kasutajad kolme erinevasse kategooriasse: <b>madal</b>, <b>keskmine</b> ja <b>kõrge</b>.
          </p>
          <p>
            <div class="text-white">a</div>
          </p>
          <p>
            Usaldusväärsuse hinne sõltub kahest põhitegurist, mis annab tervikliku pildi kasutaja usaldusväärsusest meie platvormil:
          </p>
          <p>
            <div class="text-white">a</div>
          </p>
          <ul>
            <li>
              <b>Edukad tehingud:</b> Usaldusväärsuse hindamisel on üks faktor edukate tehingute arv. Olenemata sellest, kas laenutate või laenate elektroonikat, näitab suurem edukate tehingute hulk usaldusväärsust ja ausust. Mida rohkem edukaid vahetusi teevad kasutajad, seda kõrgemale tõuseb ka nende usaldusväärsuse hinnang.
            </li>
            <p>
            <div class="text-white">a</div>
          </p>
            <li>
              <b>Kaebused:</b> Seevastu kasutaja kohta esitatud kaebuste arv võib mõjutada tema usaldusväärsust. Kaebuste suur arv on punane lipp, mis vähendab kasutaja usaldusskoori.
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";

export default {
  components: {
    Navbar,
  },
};
</script>

<style scoped>
.background {
  background-image: url("../assets/background.png");
}
</style>
