<template>
  <div class="p-4">
    <div class="flex justify-between items-center">
      <router-link to="/" class="nav-button" style="font-size: 1.5rem; padding: 1rem;">ElectronicsSwap</router-link>
      <div class="flex space-x-4 items-center">
        <router-link to="/laenutamine" class="nav-button">Laenutamine</router-link>
        <router-link to="/vahetus" class="nav-button">Vahetus</router-link>
        <router-link to="/loo_pakkumine" class="nav-button">Loo pakkumine</router-link>
        <router-link to="/ostukorv" class="nav-button">Ostukorv</router-link>
        <div class="h-10 w-10 rounded-full overflow-hidden">
          <img src="" alt="User Picture" class="h-full w-full object-cover" />
        </div>
        <router-link to="/user" class="nav-button">Username</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
};
</script>

<style scoped>
.nav-button {
  background-color: transparent;
  border: none;
  color: #2d3748;
  cursor: pointer;
  margin-right: 10px;
}

.nav-button:hover {
  background-color: #e2e8f0;
}
</style>
