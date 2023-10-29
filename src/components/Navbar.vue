<template>
  <div class="p-4">
    <div class="flex justify-between items-center">
      <button class="nav-button" style="font-size: 1.5rem; padding: 1rem;">ElectronicsSwap</button>
      <div class="flex space-x-4 items-center">
        <button class="nav-button">Laenutamine</button>
        <button class="nav-button">Vahetus</button>
        <button class="nav-button">Loo pakkumine</button>
        <button class="nav-button">Ostukorv</button>
        <div class="h-10 w-10 rounded-full overflow-hidden">
          <img src="@/assets/man.jpg" alt="User Picture" class="h-full w-full object-cover" />
        </div>
        <button class="nav-button">Username</button>
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
