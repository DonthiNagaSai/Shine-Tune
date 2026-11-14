// Copies the built game into www/ and appends the native bridge.
// Run from app/:  npm run copy:web
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, "..", "..");

const BRIDGE = `
<script>
/* Hardware back button: let the game close a sheet or pause; exit only when it
   says it has nothing left to close. */
(function () {
  function wire() {
    var app = window.Capacitor && window.Capacitor.Plugins && window.Capacitor.Plugins.App;
    if (!app || !app.addListener) return;
    app.addListener("backButton", function () {
      var handled = window.ShineTuneBack && window.ShineTuneBack();
      if (!handled) app.exitApp();
    });
  }
  if (window.Capacitor) wire();
  else document.addEventListener("DOMContentLoaded", wire);
})();
</script>
`;

const html = readFileSync(join(root, "index.html"), "utf8");
if (!html.includes("</body>")) throw new Error("index.html has no </body>");
const out = html.replace("</body>", BRIDGE + "</body>");

mkdirSync(join(here, "..", "www"), { recursive: true });
writeFileSync(join(here, "..", "www", "index.html"), out);
console.log(`www/index.html written (${Math.round(out.length / 1024)} KB)`);
