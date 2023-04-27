self.addEventListener("push", (e) => {
  console.log(e);
  const data = e.data.json();
  self.registration.showNotification(data.title, {
    body: data.body,
    icon: data.icon,
  });
});
