/* Small, progressively enhanced interactions. Content and navigation work without JS. */
document.documentElement.classList.add("js");

document.addEventListener("DOMContentLoaded", () => {
  const mobileMenu = document.querySelector(".mobile-nav");
  if (mobileMenu) {
    const label = mobileMenu.querySelector(".mobile-nav-toggle-label");
    const summary = mobileMenu.querySelector("summary");

    mobileMenu.addEventListener("toggle", () => {
      label.textContent = mobileMenu.open ? "Close" : "Menu";
    });
    mobileMenu.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        mobileMenu.open = false;
      });
    });
    document.addEventListener("pointerdown", (event) => {
      if (mobileMenu.open && !mobileMenu.contains(event.target))
        mobileMenu.open = false;
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && mobileMenu.open) {
        mobileMenu.open = false;
        summary.focus();
      }
    });
    window.addEventListener("resize", () => {
      if (window.innerWidth > 1100 && mobileMenu.open) mobileMenu.open = false;
    });
  }

  const buttons = [...document.querySelectorAll("[data-filter]")];
  if (!buttons.length) return;

  const cards = [...document.querySelectorAll(".project-filterable")];
  const groups = [...document.querySelectorAll("[data-filter-section]")];
  const count = document.getElementById("project-count");

  function show(filter) {
    let visible = 0;
    cards.forEach((card) => {
      card.hidden = filter !== "all" && card.dataset.category !== filter;
      if (!card.hidden) visible += 1;
    });
    groups.forEach((group) => {
      group.hidden = !group.querySelector(".project-filterable:not([hidden])");
    });
    buttons.forEach((button) => {
      const active = button.dataset.filter === filter;
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-pressed", String(active));
    });
    count.textContent = `SHOWING ${visible} ${visible === 1 ? "PROJECT" : "PROJECTS"}`;
  }

  buttons.forEach((button) =>
    button.addEventListener("click", () => show(button.dataset.filter)),
  );
  window.addEventListener("hashchange", () => {
    const target = document.getElementById(
      decodeURIComponent(location.hash.slice(1)),
    );
    if (target?.classList.contains("project-filterable") && target.hidden)
      show("all");
  });
});
