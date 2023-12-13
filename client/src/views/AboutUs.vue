<template>
  <div class="flex flex-col background">
    <Navbar />
    <div class="flex-grow flex items-center justify-center mt-32 text-2xl">
      <div class="bg-white p-8 rounded shadow-2xl max-w-3xl w-3/4 h-auto mb-8 extra">
        <h1 class="text-3xl font-semibold mb-4">Meist - ElectronicsSwap</h1>
        <p>
          Tere tulemast ElectronicsSwap'i, kus viimane tehnoloogia kohtub jagamismajandusega. Me usume, et tehnoloogilised seadmed peaksid olema kättesaadavad kõigile, ning oleme loonud platvormi, mis võimaldab sul rentida seadmeid teistelt tehnikahuvilistelt.
        </p>
        <h2 class="my-4 mt-8">Meie lugu</h2>
        <p>
          ElectronicsSwap on sinu usaldusväärne sihtkoht elektroonikaseadmete rentimiseks. Oleme loonud platvormi, mis võimaldab teil jagada ja kogeda uusimaid vidinaid ilma vajaduseta neid omada.
        </p>
        <h2 class="my-4 mt-8">Meie missioon</h2>
        <p>
          ElectronicsSwap'i missiooniks on luua tehnikahuviliste kogukond, kes saavad jagada ja kogeda viimaseid vidinaid ilma omamise vajaduseta. Meie eesmärk on vähendada elektroonikaromu, edendada säästlikkust ning pakkuda taskukohast võimalust inimestele, kes soovivad nautida tipptasemel tehnoloogiat.
        </p>
        <h2 class="my-4 mt-8">Kuidas see toimib?</h2>
        <p>
          ElectronicsSwap'i kasutamine on lihtne. Kasutajad saavad postitada oma elektroonikaseadmed rendile, määrates ise tingimused. Olgu sul vaja kõrgekvaliteedilist kaamerat, mängukonsooli või nutikella – meie platvormil on mitmekesine valik seadmeid. Rendile võtmine on lihtne, turvaline ja kuluefektiivne.
        </p>
        <h2 class="my-4 mt-8">Miks valida ElectronicsSwap'i?</h2>
        <ul>
          <li><b>Lai valik seadmeid:</b> Avasta mitmekesine valik elektroonikaseadmeid rendiks.</li>
          <li><b>Kogukonnapõhine:</b> Ühendu teiste tehnikahuvilistega ja loo jagamiskogukond.</li>
          <li><b>Jätkusuutlik:</b> Aita vähendada elektroonikaromu ja edenda säästlikumat eluviisi.</li>
          <li><b>Taskukohane:</b> Naudi uusimat tehnoloogiat ilma omamise kõrgete kuludeta.</li>
          <li><b>Turvalised tehingud:</b> Meie platvorm tagab turvalised tehingud ja kasutajate kontrolli.</li>
        </ul>
        <h2 class="my-4 mt-8">Võta meiega ühendust</h2>
        <p>
          Kui sul on küsimusi, tagasisidet või päringuid,
          <router-link v-if="isLoggedIn"
          class="custom-button"
          to="/abi">võta meiega julgesti ühendust.</router-link>
          <router-link v-else
          class="custom-button"
          to="/login">võta meiega julgesti ühendust.</router-link>
          Oleme siin, et sind aidata!
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
import { useAuthStore } from '@/store/modules/auth';
import { mapGetters } from 'pinia'

export default {
  components: {
    Navbar,
  },
  data: () => ({
    authStore: useAuthStore(),
  }),
  computed: {
    ...mapGetters(useAuthStore, ['isLoggedIn']),
  },
};
</script>

<style scoped>
.background {
  background-image: url("../assets/background.png");
}
.extra h2{
    font-weight: 600;
}
.extra b{
  font-weight: 530;
}
.extra li{
  margin-bottom: 4px;
}
.extra ul{
  list-style-type: disc;
  margin-left: 20px;
}
.custom-button {
  transition: background-color 0.5s ease, border-color 0.5s ease,
    color 0.5s ease, transform 0.5s ease;
  display: inline-block;
  color: #9aa2ea;
  cursor: pointer;
}
.custom-button:hover {
  color: #ceb4ef;
}
</style>
