import { categoryColors, categoryOrder, deckTitle, people } from "./data.mjs";

const BG = "#F6F7F4";
const INK = "#172033";
const MUTED = "#64748B";
const LINE = "#D9E0E7";
const WHITE = "#FFFFFF";
const FONT = "Apple SD Gothic Neo";

function addText(ctx, slide, text, frame, opts = {}) {
  return ctx.addText(slide, {
    text,
    ...frame,
    fontSize: opts.fontSize ?? 18,
    color: opts.color ?? INK,
    bold: opts.bold ?? false,
    typeface: FONT,
    fill: opts.fill ?? "#00000000",
    line: ctx.line("#00000000", 0),
    insets: opts.insets ?? { left: 0, right: 0, top: 0, bottom: 0 },
    valign: opts.valign ?? "top",
    align: opts.align ?? "left",
  });
}

function addRect(ctx, slide, frame, opts = {}) {
  return ctx.addShape(slide, {
    ...frame,
    geometry: opts.geometry ?? "rect",
    fill: opts.fill ?? WHITE,
    line: opts.line ?? ctx.line(LINE, 1),
  });
}

function clean(value) {
  return String(value || "").replace(/\s+/g, " ").trim();
}

function shorten(value, max = 84) {
  const text = clean(value);
  if (text.length <= max) return text;
  return `${text.slice(0, max - 1).trim()}…`;
}

function groupedPeople() {
  return categoryOrder
    .map((category) => ({
      category,
      items: people.filter((person) => person.category === category),
    }))
    .filter((group) => group.items.length > 0);
}

function slideBase(presentation, ctx, options = {}) {
  const slide = presentation.slides.add();
  addRect(ctx, slide, { x: 0, y: 0, w: ctx.W, h: ctx.H }, { fill: BG, line: ctx.line("#00000000", 0) });
  if (options.category) {
    const color = categoryColors[options.category] ?? categoryColors["미분류"];
    addRect(ctx, slide, { x: 0, y: 0, w: 16, h: ctx.H }, { fill: color.accent, line: ctx.line(color.accent, 0) });
  }
  addText(ctx, slide, `Codex Impact Workshop · ${deckTitle}`, { x: 60, y: 674, w: 760, h: 18 }, {
    fontSize: 11,
    color: "#8A94A6",
  });
  addText(ctx, slide, `${options.index ?? ""}`.trim(), { x: 1160, y: 672, w: 60, h: 18 }, {
    fontSize: 11,
    color: "#8A94A6",
    align: "right",
  });
  return slide;
}

export async function renderIntroSlide(presentation, ctx) {
  const slide = slideBase(presentation, ctx, { index: "01" });
  addText(ctx, slide, "선발 사회혁신가 소개", { x: 60, y: 40, w: 640, h: 48 }, {
    fontSize: 42,
    bold: true,
  });
  addText(ctx, slide, "과제 분류 기준 그룹핑 · 사회혁신가 15명", { x: 62, y: 92, w: 520, h: 26 }, {
    fontSize: 18,
    color: MUTED,
  });

  const counts = groupedPeople();
  const chipLayout = [
    { x: 720, y: 50 },
    { x: 950, y: 50 },
    { x: 720, y: 86 },
    { x: 950, y: 86 },
  ];
  counts.forEach((group, index) => {
    const color = categoryColors[group.category];
    const label = `${group.category.replace("·", " · ")} ${group.items.length}`;
    const spot = chipLayout[index] ?? { x: 950, y: 86 };
    addRect(ctx, slide, { x: spot.x, y: spot.y, w: 220, h: 28 }, { fill: color.pale, line: ctx.line(color.accent, 1) });
    addText(ctx, slide, label, { x: spot.x + 10, y: spot.y + 8, w: 200, h: 14 }, {
      fontSize: 12,
      color: color.dark,
      bold: true,
      align: "center",
    });
  });

  const x = 60;
  const y0 = 140;
  const widths = [260, 160, 300, 270];
  const headers = ["과제 분류", "이름", "소속", "역할/직함"];
  addRect(ctx, slide, { x, y: y0, w: 1120, h: 32 }, { fill: "#172033", line: ctx.line("#172033", 0) });
  let cx = x;
  headers.forEach((header, idx) => {
    addText(ctx, slide, header, { x: cx + 12, y: y0 + 8, w: widths[idx] - 18, h: 16 }, {
      fontSize: 13,
      color: WHITE,
      bold: true,
    });
    cx += widths[idx];
  });

  let rowY = y0 + 32;
  groupedPeople().forEach((group) => {
    const color = categoryColors[group.category];
    group.items.forEach((person, index) => {
      const fill = index % 2 === 0 ? WHITE : "#FBFCFE";
      addRect(ctx, slide, { x, y: rowY, w: 1120, h: 30 }, { fill, line: ctx.line(LINE, 0.8) });
      addRect(ctx, slide, { x, y: rowY, w: 8, h: 30 }, { fill: color.accent, line: ctx.line(color.accent, 0) });
      const cells = [
        person.category,
        person.name,
        shorten(person.org, 26),
        shorten(person.role, 28),
      ];
      cx = x;
      cells.forEach((cell, idx) => {
        addText(ctx, slide, cell, { x: cx + 14, y: rowY + 8, w: widths[idx] - 20, h: 16 }, {
          fontSize: idx === 1 ? 14 : 13,
          color: idx === 0 ? color.dark : INK,
          bold: idx <= 1,
        });
        cx += widths[idx];
      });
      rowY += 30;
    });
  });

  addText(ctx, slide, "연락처와 이메일은 개인정보 보호를 위해 제외했습니다.", { x: 62, y: 636, w: 560, h: 22 }, {
    fontSize: 13,
    color: MUTED,
  });
  return slide;
}

function addSection(ctx, slide, label, body, x, y, w, color, compact = false) {
  addText(ctx, slide, label, { x, y, w, h: 20 }, {
    fontSize: 13,
    bold: true,
    color: color.dark,
  });
  addRect(ctx, slide, { x, y: y + 22, w, h: compact ? 66 : 76 }, {
    fill: WHITE,
    line: ctx.line("#E2E8F0", 1),
  });
  addText(ctx, slide, body, { x: x + 14, y: y + 34, w: w - 28, h: compact ? 48 : 56 }, {
    fontSize: compact ? 14 : 15,
    color: INK,
    insets: { left: 0, right: 0, top: 0, bottom: 0 },
  });
}

export async function renderPersonSlide(presentation, ctx, personIndex) {
  const person = people[personIndex];
  const color = categoryColors[person.category] ?? categoryColors["미분류"];
  const slide = slideBase(presentation, ctx, { category: person.category, index: String(personIndex + 2).padStart(2, "0") });

  addText(ctx, slide, person.name, { x: 60, y: 38, w: 260, h: 54 }, {
    fontSize: 42,
    bold: true,
  });
  addText(ctx, slide, `${person.org} · ${person.role}`, { x: 64, y: 92, w: 620, h: 24 }, {
    fontSize: 18,
    color: MUTED,
  });
  addRect(ctx, slide, { x: 880, y: 48, w: 300, h: 34 }, { fill: color.pale, line: ctx.line(color.accent, 1.2) });
  addText(ctx, slide, person.category, { x: 898, y: 57, w: 264, h: 16 }, {
    fontSize: 14,
    bold: true,
    color: color.dark,
    align: "center",
  });

  addRect(ctx, slide, { x: 60, y: 138, w: 1120, h: 1.5 }, { fill: color.accent, line: ctx.line(color.accent, 0) });

  const leftX = 70;
  const rightX = 630;
  addSection(ctx, slide, "참여 동기", person.motive, leftX, 164, 500, color);
  addSection(ctx, slide, "해결하고 싶은 문제", person.problem, rightX, 164, 500, color);
  addSection(ctx, slide, "현재 처리 방식", person.current, leftX, 268, 500, color);
  addSection(ctx, slide, "반복 업무 / 병목 / 비용·시간 낭비", person.bottleneck, rightX, 268, 500, color);
  addSection(ctx, slide, "개발자와 함께 해보고 싶은 일", person.build, leftX, 372, 500, color);
  addSection(ctx, slide, "해결 후 기대 변화", person.impact, rightX, 372, 500, color);

  addRect(ctx, slide, { x: 70, y: 582, w: 1060, h: 1 }, { fill: "#CBD5E1", line: ctx.line("#CBD5E1", 0) });
  addText(ctx, slide, "소개 포인트", { x: 70, y: 604, w: 100, h: 18 }, {
    fontSize: 13,
    bold: true,
    color: color.dark,
  });
  addText(ctx, slide, `${person.category} · ${shorten(person.problem, 110)}`, { x: 170, y: 604, w: 950, h: 20 }, {
    fontSize: 13,
    color: MUTED,
  });
  return slide;
}
