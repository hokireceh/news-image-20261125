import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// Copy the rendered front page (entry.png, next to this script) into the
// output directory make.fun expects. Deterministic, stdlib only, no network.
// Defaults to "out" when MAKEFUN_OUTPUT_DIR is unset, then exits 0.
const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR || "out";
const target = join(outDir, "entry.png");

mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);
console.log(`copied entry.png -> ${target}`);
