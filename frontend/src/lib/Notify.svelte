<script lang="ts">
  import { urlBase64ToUint8Array, PUBLIC_VAPID_KEY } from "./helpers";

  const sendNotification = () => {
    if ("Notification" in window) {
      if (window.Notification.permission !== "granted") {
        alert("Notification permission is not granted.");
      }
      new window.Notification("Dupa test!");
    }
  };

  const subscribeToWebPush = async () => {
    if ("serviceWorker" in navigator) {
      const registration = await navigator.serviceWorker.ready;
      const subscription = await registration.pushManager.subscribe({
        userVisibleOnly: true,
        applicationServerKey: urlBase64ToUint8Array(PUBLIC_VAPID_KEY),
      });
      console.log(subscription);

      await fetch("http://localhost:5000/subscription", {
        method: "POST",
        body: JSON.stringify(subscription),
        headers: {
          "content-type": "application/json",
        },
      });
    }
  };

  const askForPermission = () => {
    if ("Notification" in window) {
      // Asks only if permission hasnt been granted
      window.Notification.requestPermission();
    }
  };

  const sendWebPushNotification = async () => {
    await fetch("http://localhost:5000/broadcast", {
      method: "GET",
      headers: {
        "content-type": "application/json",
      },
    });
  };
</script>

<div>
  <button on:click={askForPermission}> Ask for permission </button>
  <button on:click={subscribeToWebPush}> Subscribe to web push </button>
  <button on:click={sendNotification}> Send notification via Window </button>
  <button on:click={sendWebPushNotification}>
    Send notification via Service Worker
  </button>
</div>
