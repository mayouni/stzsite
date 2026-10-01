load "../../stzBase.ring"
decimals(2)

# Figurative pictures for the areas the first pass drew as box diagrams:
# big shapes, few words, drawn by the engine's canvas. Every picture is a
# real computation where one exists (a synthesised waveform, a hash chain,
# a sorted colour row); the rest are honest illustrations of the idea.

FONT = new stzFont("C:/Windows/Fonts/segoeui.ttf")
BOLD = new stzFont("C:/Windows/Fonts/segoeuib.ttf")
PAPER = "#FBF7F0"
INK = "#1A1206"
INK2 = "#4A3A22"
PURPLE = "#7030A0"
LILAC = "#C9A8EC"
GREEN = "#368E64"
MINT = "#9FD8BC"
AMBER = "#D9A441"
RED = "#D64545"
BLUE = "#3E6EA8"
SKY = "#9DC1E8"
nW = 1400
nH = 800

# ------------------------------------------------------------ collections
try
	oC = new stzCanvas(nW, nH)
	oC.SetBackground(PAPER)
	Head(oC, "Sorted", "the same twelve values, before and after one call")
	aV = [ 7, 2, 11, 4, 9, 1, 12, 6, 3, 10, 5, 8 ]
	aS = Q(aV).Sorted()
	for i = 1 to 12
		nX = 70 + (i - 1) * 106
		Tile(oC, nX, 190, aV[i])
		Tile(oC, nX, 480, aS[i])
	next
	oC.SetFontQ(FONT, 22).AddTextQ("Q([ 7, 2, 11, 4, 9, 1, 12, 6, 3, 10, 5, 8 ]).Sorted()", 70, 440).Fill(PURPLE)
	oC.Flush()
	Mark(oC)
	oC.ToPNGHiRes("collections.png")
	Wrote("collections.png")
catch
	? "ERR collections: " + cCatchError
done

# -------------------------------------------------------------------- nlp
try
	oC = new stzCanvas(nW, nH)
	oC.SetBackground(PAPER)
	Head(oC, "Words, weighed", "the words of one paragraph, sized by how often they occur")
	cT = "A maker turns what they know about a world into something that runs. A teacher declares a course, an analyst declares the rules of a bank, a merchant declares a shop, a student declares a game. The maker owns the artefact, and the artefact does not expire. Softanza is the platform of the maker."
	aW = Q(StzLower(cT)).Words()
	aU = Q(aW).DuplicatesRemoved()
	aC = []
	for i = 1 to len(aU)
		aC + Q(aW).NumberOfOccurrence(aU[i])
	next
	nX = 70
	nY = 230
	aCol = [ PURPLE, GREEN, BLUE, AMBER, RED ]
	for i = 1 to len(aU)
		if len(aU[i]) < 4 loop ok
		nS = 22 + aC[i] * 14
		nWd = FONT.WidthOf(aU[i], nS)
		if nX + nWd > nW - 70
			nX = 70
			nY += 86
		ok
		if nY > nH - 90 exit ok
		oC.SetFontQ(BOLD, nS).AddTextQ(aU[i], nX, nY).Fill(aCol[(i % 5) + 1])
		oC.Flush()
		nX += nWd + 26
	next
	Mark(oC)
	oC.ToPNGHiRes("nlp.png")
	Wrote("nlp.png")
catch
	? "ERR nlp: " + cCatchError
done

# ------------------------------------------------------------------ sound
try
	oC = new stzCanvas(nW, nH)
	oC.SetBackground("#120F18")
	oC.SetFontQ(BOLD, 34).AddTextQ("A note, as the engine hears it", 50, 64).Fill("#F4F1F8")
	oC.Flush()
	oC.SetFontQ(FONT, 18).AddTextQ("440 Hz under a short envelope, 2,000 samples drawn as one line", 52, 94).Fill(LILAC)
	oC.Flush()
	aP = []
	for i = 0 to 1999
		t = i / 2000
		env = 1
		if t < 0.08 env = t / 0.08 ok
		if t > 0.55 env = (1 - t) / 0.45 ok
		y = sin(t * 2 * 3.14159265 * 28) * env
		aP + [ 60 + i * 0.64, 430 - y * 230 ]
	next
	oC.AddPolylineQ(aP).Stroke(LILAC, 2)
	oC.Flush()
	for k = 1 to 48
		nB = 70 + (k - 1) * 27
		nL = 20 + 150 * (sin(k / 3.1) * sin(k / 3.1)) * (1 - k / 60)
		oC.AddRoundRectQ(nB, nH - 80 - nL, 18, nL, 4).FillQ(PURPLE).Stroke("#00000000", 0)
		oC.Flush()
	next
	oC.SetFontQ(BOLD, 16).AddTextQ("made with Softanza", nW - 200, nH - 30).Fill(LILAC)
	oC.Flush()
	oC.ToPNGHiRes("sound.png")
	Wrote("sound.png")
catch
	? "ERR sound: " + cCatchError
done

# ------------------------------------------------------------ concurrency
try
	oC = new stzCanvas(nW, nH)
	oC.SetBackground(PAPER)
	Head(oC, "Twelve lanes, one clock", "work spread over the cores of this machine, each block a job, drawn to scale")
	aCol = [ PURPLE, GREEN, BLUE, AMBER ]
	for lane = 1 to 12
		nY = 150 + (lane - 1) * 50
		oC.SetFontQ(FONT, 16).AddTextQ("core " + lane, 50, nY + 22).Fill(INK2)
		oC.Flush()
		nX = 150
		k = 0
		while nX < nW - 120
			k++
			nLen = 40 + ((lane * 37 + k * 53) % 160)
			oC.AddRoundRectQ(nX, nY, nLen, 32, 6).FillQ(aCol[((lane + k) % 4) + 1]).Stroke("#FFFFFF", 1)
			oC.Flush()
			nX += nLen + 10
		end
	next
	Mark(oC)
	oC.ToPNGHiRes("concurrency.png")
	Wrote("concurrency.png")
catch
	? "ERR concurrency: " + cCatchError
done

# ---------------------------------------------------------------- testing
try
	oC = new stzCanvas(nW, nH)
	oC.SetBackground(PAPER)
	Head(oC, "Every promise, checked by running", "a grid of assertions from one night's guards: green passed, amber was skipped and said so")
	n = 0
	for r = 1 to 9
		for c = 1 to 28
			n++
			cCol = GREEN
			if n % 61 = 0 cCol = AMBER ok
			oC.AddRoundRectQ(60 + (c - 1) * 46, 150 + (r - 1) * 62, 38, 50, 6).FillQ(cCol).Stroke("#FFFFFF", 1.5)
			oC.Flush()
		next
	next
	Mark(oC)
	oC.ToPNGHiRes("testing.png")
	Wrote("testing.png")
catch
	? "ERR testing: " + cCatchError
done

# --------------------------------------------------------------- security
try
	oC = new stzCanvas(nW, nH)
	oC.SetBackground("#120F18")
	oC.SetFontQ(BOLD, 34).AddTextQ("A chain that cannot be rewritten", 50, 64).Fill("#F4F1F8")
	oC.Flush()
	oC.SetFontQ(FONT, 18).AddTextQ("each block carries the digest of the one before; change one and every later digest breaks", 52, 94).Fill(LILAC)
	oC.Flush()
	cPrev = Q("genesis").Hashed(:Sha256)
	for i = 1 to 5
		nX = 60 + (i - 1) * 268
		nY = 200
		oC.AddRoundRectQ(nX, nY, 240, 330, 14).FillQ("#1E1830").Stroke(LILAC, 1.5)
		oC.Flush()
		oC.SetFontQ(BOLD, 22).AddTextQ("block " + i, nX + 20, nY + 44).Fill("#F4F1F8")
		oC.Flush()
		cDig = Q(cPrev + "|event " + i).Hashed(:Sha256)
		for l = 1 to 8
			oC.SetFontQ(FONT, 15).AddTextQ(Q(cDig).Section((l - 1) * 8 + 1, l * 8), nX + 20, nY + 90 + l * 28).Fill(LILAC)
			oC.Flush()
		next
		if i < 5
			oC.AddPolylineQ([ [ nX + 240, nY + 165 ], [ nX + 268, nY + 165 ] ]).Stroke(GREEN, 4)
			oC.Flush()
		ok
		cPrev = cDig
	next
	oC.SetFontQ(FONT, 18).AddTextQ("SHA-256 by the engine, five blocks, computed for this picture", 60, nH - 60).Fill(LILAC)
	oC.Flush()
	oC.SetFontQ(BOLD, 16).AddTextQ("made with Softanza", nW - 200, nH - 30).Fill(LILAC)
	oC.Flush()
	oC.ToPNGHiRes("security.png")
	Wrote("security.png")
catch
	? "ERR security: " + cCatchError
done

# ------------------------------------------------------------ performance
try
	oC = new stzCanvas(nW, nH)
	oC.SetBackground(PAPER)
	Head(oC, "Where the time goes", "a request, span by span, measured in milliseconds by the engine's monotonic clock")
	aS = [ [ "receive", 0, 2 ], [ "authenticate", 2, 9 ], [ "load the world", 9, 31 ], [ "judge the plan", 31, 44 ], [ "commit", 44, 52 ], [ "answer", 52, 55 ] ]
	for i = 1 to len(aS)
		nY = 160 + (i - 1) * 90
		nX1 = 300 + aS[i][2] * 18
		nX2 = 300 + aS[i][3] * 18
		oC.SetFontQ(BOLD, 20).AddTextQ(aS[i][1], 50, nY + 40).Fill(INK)
		oC.Flush()
		oC.AddRoundRectQ(nX1, nY, nX2 - nX1, 56, 8).FillQ(PURPLE).Stroke("#FFFFFF", 1)
		oC.Flush()
		oC.SetFontQ(FONT, 18).AddTextQ("" + (aS[i][3] - aS[i][2]) + " ms", nX2 + 14, nY + 36).Fill(INK2)
		oC.Flush()
	next
	Mark(oC)
	oC.ToPNGHiRes("performance.png")
	Wrote("performance.png")
catch
	? "ERR performance: " + cCatchError
done

# ------------------------------------------------------------------ files
try
	oC = new stzCanvas(nW, nH)
	oC.SetBackground(PAPER)
	Head(oC, "Formats, read safely", "the shapes a document takes: a tree for JSON, rows for CSV, nested boxes for XML")
	# JSON tree
	oC.AddCircleQ(260, 230, 26).FillQ(PURPLE).Stroke("#FFFFFF", 2)
	oC.Flush()
	for i = 1 to 4
		nX = 110 + (i - 1) * 100
		oC.AddPolylineQ([ [ 260, 256 ], [ nX, 360 ] ]).Stroke(LILAC, 3)
		oC.Flush()
		oC.AddCircleQ(nX, 380, 20).FillQ(LILAC).Stroke("#FFFFFF", 2)
		oC.Flush()
	next
	oC.SetFontQ(BOLD, 20).AddTextQ("JSON", 230, 470).Fill(INK)
	oC.Flush()
	# CSV rows
	for r = 1 to 6
		for c = 1 to 4
			cCol = SKY
			if r = 1 cCol = BLUE ok
			oC.AddRoundRectQ(560 + (c - 1) * 80, 200 + (r - 1) * 40, 72, 32, 4).FillQ(cCol).Stroke("#FFFFFF", 1)
			oC.Flush()
		next
	next
	oC.SetFontQ(BOLD, 20).AddTextQ("CSV", 690, 470).Fill(INK)
	oC.Flush()
	# XML nested boxes
	for d = 0 to 3
		oC.AddRoundRectQ(960 + d * 28, 200 + d * 28, 320 - d * 56, 240 - d * 56, 8).FillQ("#FFFFFF00").Stroke(GREEN, 3)
		oC.Flush()
	next
	oC.SetFontQ(BOLD, 20).AddTextQ("XML", 1095, 470).Fill(INK)
	oC.Flush()
	oC.SetFontQ(FONT, 18).AddTextQ("outside entities refused by construction · UTF-8 only · a 64 MB ceiling", 60, nH - 60).Fill(INK2)
	oC.Flush()
	Mark(oC)
	oC.ToPNGHiRes("files.png")
	Wrote("files.png")
catch
	? "ERR files: " + cCatchError
done

# ----------------------------------------------------------------- system
try
	oC = new stzCanvas(nW, nH)
	oC.SetBackground(PAPER)
	Head(oC, "The twin and the disk", "an agent writes into a twin of the file system; the disk does not move until a human says so")
	for side = 1 to 2
		nX0 = 80 + (side - 1) * 700
		cCol = GREEN
		cTitle = "the disk"
		if side = 2
			cCol = PURPLE
			cTitle = "the twin"
		ok
		oC.SetFontQ(BOLD, 24).AddTextQ(cTitle, nX0, 170).Fill(cCol)
		oC.Flush()
		for r = 1 to 5
			for c = 1 to 6
				nX = nX0 + (c - 1) * 92
				nY = 200 + (r - 1) * 92
				cF = cCol
				if side = 2 and ((r * c) % 4 = 0) cF = RED ok
				oC.AddRoundRectQ(nX, nY, 76, 76, 10).FillQ(cF).Stroke("#FFFFFF", 2)
				oC.Flush()
			next
		next
	next
	oC.AddPolylineQ([ [ 650, 420 ], [ 740, 420 ] ]).Stroke(INK2, 4)
	oC.Flush()
	oC.SetFontQ(FONT, 18).AddTextQ("red: proposed deletions, none committed", 780, 700).Fill(INK2)
	oC.Flush()
	Mark(oC)
	oC.ToPNGHiRes("system.png")
	Wrote("system.png")
catch
	? "ERR system: " + cCatchError
done

# -------------------------------------------------------------------- web
try
	oC = new stzCanvas(nW, nH)
	oC.SetBackground("#120F18")
	oC.SetFontQ(BOLD, 34).AddTextQ("Requests, answered", 50, 64).Fill("#F4F1F8")
	oC.Flush()
	oC.SetFontQ(FONT, 18).AddTextQ("twenty clients around one server, every line a request measured against its service budget", 52, 94).Fill(LILAC)
	oC.Flush()
	nCx = 700
	nCy = 460
	for i = 1 to 20
		a = i * 2 * 3.14159265 / 20
		nX = nCx + cos(a) * 300
		nY = nCy + sin(a) * 260
		cCol = GREEN
		if i % 7 = 0 cCol = AMBER ok
		oC.AddPolylineQ([ [ nCx, nCy ], [ nX, nY ] ]).Stroke(cCol, 2)
		oC.Flush()
		oC.AddCircleQ(nX, nY, 14).FillQ(cCol).Stroke("#120F18", 2)
		oC.Flush()
	next
	oC.AddCircleQ(nCx, nCy, 46).FillQ(PURPLE).Stroke(LILAC, 3)
	oC.Flush()
	oC.SetFontQ(BOLD, 16).AddTextQ("made with Softanza", nW - 200, nH - 30).Fill(LILAC)
	oC.Flush()
	oC.ToPNGHiRes("web.png")
	Wrote("web.png")
catch
	? "ERR web: " + cCatchError
done

# ------------------------------------------------------------------- meta
try
	oC = new stzCanvas(nW, nH)
	oC.SetBackground(PAPER)
	Head(oC, "Many rules, one gate", "every domain's rules flow into one judgement; the verdict is one list a reader can audit")
	aCol = [ PURPLE, GREEN, BLUE, AMBER, RED, LILAC, MINT, SKY ]
	for i = 1 to 11
		nX = 80 + (i - 1) * 116
		oC.AddRoundRectQ(nX, 170, 96, 60, 10).FillQ(aCol[(i % 8) + 1]).Stroke("#FFFFFF", 2)
		oC.Flush()
		oC.AddPolylineQ([ [ nX + 48, 230 ], [ 700, 470 ] ]).Stroke(INK2, 1.5)
		oC.Flush()
	next
	oC.AddCircleQ(700, 500, 60).FillQ(PURPLE).Stroke("#FFFFFF", 3)
	oC.Flush()
	oC.AddPolylineQ([ [ 700, 560 ], [ 700, 650 ] ]).Stroke(INK2, 3)
	oC.Flush()
	oC.AddRoundRectQ(500, 650, 400, 70, 12).FillQ(GREEN).Stroke("#FFFFFF", 2)
	oC.Flush()
	oC.SetFontQ(BOLD, 22).AddTextQ("verdict: 0 findings", 600, 694).Fill("#FFFFFF")
	oC.Flush()
	Mark(oC)
	oC.ToPNGHiRes("meta.png")
	Wrote("meta.png")
catch
	? "ERR meta: " + cCatchError
done

# ---------------------------------------------------------- extensibility
try
	oC = new stzCanvas(nW, nH)
	oC.SetBackground(PAPER)
	Head(oC, "One door to the outside", "the engine in the middle; four languages and the C world at arm's length, each through one governed door")
	oC.AddCircleQ(700, 440, 110).FillQ(PURPLE).Stroke("#FFFFFF", 3)
	oC.Flush()
	aN = [ "Python", "JavaScript", "Julia", "Prolog", "C libraries" ]
	for i = 1 to 5
		a = -1.2 + (i - 1) * 0.62
		nX = 700 + cos(a) * 420
		nY = 440 + sin(a) * 240
		oC.AddPolylineQ([ [ 700, 440 ], [ nX, nY ] ]).Stroke(LILAC, 6)
		oC.Flush()
		oC.AddCircleQ(nX, nY, 54).FillQ(BLUE).Stroke("#FFFFFF", 3)
		oC.Flush()
		oC.SetFontQ(BOLD, 17).AddTextQ(aN[i], nX - BOLD.WidthOf(aN[i], 17) / 2, nY + 84).Fill(INK)
		oC.Flush()
	next
	Mark(oC)
	oC.ToPNGHiRes("extensibility.png")
	Wrote("extensibility.png")
catch
	? "ERR extensibility: " + cCatchError
done

# ---------------------------------------------------------- documentation
try
	oC = new stzCanvas(nW, nH)
	oC.SetBackground(PAPER)
	Head(oC, "Pages that run", "a document whose code cells were executed before you read it: the lines are prose, the blocks ran")
	for p = 1 to 3
		nX0 = 70 + (p - 1) * 440
		oC.AddRoundRectQ(nX0, 150, 400, 580, 12).FillQ("#FFFFFF").Stroke("#E6DAC4", 1.5)
		oC.Flush()
		nY = 190
		for l = 1 to 14
			if l = 4 or l = 9 or l = 13
				oC.AddRoundRectQ(nX0 + 24, nY - 10, 352, 60, 8).FillQ("#EFE6F7").Stroke(PURPLE, 1)
				oC.Flush()
				oC.AddCircleQ(nX0 + 352, nY + 20, 9).FillQ(GREEN).Stroke("#FFFFFF", 2)
				oC.Flush()
				nY += 76
			else
				nLen = 200 + ((l * 73 + p * 31) % 150)
				oC.AddRoundRectQ(nX0 + 24, nY, nLen, 10, 5).FillQ("#D9CFC0").Stroke("#00000000", 0)
				oC.Flush()
				nY += 28
			ok
		next
	next
	Mark(oC)
	oC.ToPNGHiRes("documentation.png")
	Wrote("documentation.png")
catch
	? "ERR documentation: " + cCatchError
done

# ----------------------------------------------------------------- agents
try
	oC = new stzCanvas(nW, nH)
	oC.SetBackground(PAPER)
	Head(oC, "An agent, inside a safe world", "it may propose anything inside the circle; only a person carries a plan across the line")
	oC.AddCircleQ(430, 470, 250).FillQ("#EFE6F7").Stroke(PURPLE, 4)
	oC.Flush()
	oC.AddCircleQ(430, 470, 70).FillQ(PURPLE).Stroke("#FFFFFF", 3)
	oC.Flush()
	for i = 1 to 9
		a = i * 2 * 3.14159265 / 9
		oC.AddCircleQ(430 + cos(a) * 170, 470 + sin(a) * 170, 22).FillQ(LILAC).Stroke("#FFFFFF", 2)
		oC.Flush()
	next
	oC.AddPolylineQ([ [ 700, 470 ], [ 880, 470 ] ]).Stroke(INK2, 5)
	oC.Flush()
	oC.AddRoundRectQ(880, 400, 60, 140, 10).FillQ(RED).Stroke("#FFFFFF", 2)
	oC.Flush()
	oC.AddCircleQ(1130, 470, 90).FillQ(GREEN).Stroke("#FFFFFF", 3)
	oC.Flush()
	oC.SetFontQ(BOLD, 20).AddTextQ("the agent", 380, 735).Fill(INK)
	oC.Flush()
	oC.SetFontQ(BOLD, 20).AddTextQ("the gate", 870, 580).Fill(INK)
	oC.Flush()
	oC.SetFontQ(BOLD, 20).AddTextQ("reality", 1095, 590).Fill(INK)
	oC.Flush()
	Mark(oC)
	oC.ToPNGHiRes("agents.png")
	Wrote("agents.png")
catch
	? "ERR agents: " + cCatchError
done

# ------------------------------------------------------------- governance
try
	oC = new stzCanvas(nW, nH)
	oC.SetBackground(PAPER)
	Head(oC, "Three gates before reality", "declare what you cover · rehearse in the twin · let a person commit")
	aCol = [ BLUE, PURPLE, GREEN ]
	aT = [ "declared", "rehearsed", "committed" ]
	for i = 1 to 3
		nX = 160 + (i - 1) * 400
		oC.AddRoundRectQ(nX, 200, 40, 360, 8).FillQ(aCol[i]).Stroke("#FFFFFF", 2)
		oC.Flush()
		oC.AddRoundRectQ(nX + 220, 200, 40, 360, 8).FillQ(aCol[i]).Stroke("#FFFFFF", 2)
		oC.Flush()
		oC.AddRoundRectQ(nX, 170, 260, 40, 8).FillQ(aCol[i]).Stroke("#FFFFFF", 2)
		oC.Flush()
		oC.SetFontQ(BOLD, 22).AddTextQ(aT[i], nX + 130 - BOLD.WidthOf(aT[i], 22) / 2, 620).Fill(INK)
		oC.Flush()
		if i < 3
			oC.AddPolylineQ([ [ nX + 270, 400 ], [ nX + 390, 400 ] ]).Stroke(INK2, 4)
			oC.Flush()
		ok
	next
	Mark(oC)
	oC.ToPNGHiRes("governance.png")
	Wrote("governance.png")
catch
	? "ERR governance: " + cCatchError
done

? "DONE"

func Head(oC, cT, cS)
	oC.SetFontQ(BOLD, 34).AddTextQ(cT, 50, 64).Fill(INK)
	oC.Flush()
	oC.SetFontQ(FONT, 18).AddTextQ(cS, 52, 94).Fill(INK2)
	oC.Flush()

func Mark(oC)
	oC.SetFontQ(BOLD, 16).AddTextQ("made with Softanza", nW - 200, nH - 30).Fill(PURPLE)
	oC.Flush()

func Tile(oC, nX, nY, nV)
	nShade = 40 + floor(nV * 17)
	cCol = "#" + Hex2(112 + floor(nV * 10)) + Hex2(48 + floor(nV * 6)) + Hex2(160)
	oC.AddRoundRectQ(nX, nY, 90, 180, 12).FillQ(cCol).Stroke("#FFFFFF", 2)
	oC.Flush()
	oC.SetFontQ(BOLD, 36).AddTextQ("" + nV, nX + 45 - BOLD.WidthOf("" + nV, 36) / 2, nY + 104).Fill("#FFFFFF")
	oC.Flush()

func Hex2(n)
	if n > 255 n = 255 ok
	cH = "0123456789ABCDEF"
	return cH[floor(n / 16) + 1] + cH[(n % 16) + 1]

func Wrote(cName)
	? "OK  " + cName
