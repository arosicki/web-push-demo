<script lang="ts">
  import { onMount } from "svelte";
  import Notify from "./lib/Notify.svelte";

  const registerServiceWorker = async () => {
    if ("serviceWorker" in navigator) {
      try {
        await navigator.serviceWorker.register("/sw.js");
      } catch (error) {
        console.log("Service worker registration failed:", error);
      }
    }
  };

  onMount(() => {
    registerServiceWorker();
  });
</script>

<main>
  <div class="card">
    <Notify />
  </div>
</main>
