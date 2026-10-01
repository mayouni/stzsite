load "../../stzBase.ring"
decimals(2)

# A render per area of the Atlas, drawn by the engine tonight for the
# Softanza website. Every picture is written as <slug>.png in this folder.
# One failure must not stop the others, so every picture is its own try.

FONT = new stzFont("C:/Windows/Fonts/segoeui.ttf")
BOLD = new stzFont("C:/Windows/Fonts/segoeuib.ttf")
PAPER = "#FBF7F0"
INK = "#1A1206"
INK2 = "#4A3A22"
PURPLE = "#7030A0"
GREEN = "#368E64"
RED = "#F60000"
OPT = [ :Font = FONT, :NodeWidth = 170, :NodeHeight = 58, :FontSize = 18 ]

# ---------------------------------------------------------------- string
try
	nW = 1400
	nH = 760
	oC = new stzCanvas(nW, nH)
	oC.SetBackground(PAPER)
	Title(oC, "One engine, every script", "the same call counts characters, not bytes -- shaped and measured by the engine")
	aW = [ [ "Softanza", "Latin" ], [ "سلام", "Arabic" ], [ "שלום", "Hebrew" ], [ "Ειρήνη", "Greek" ],
	       [ "Мир", "Cyrillic" ], [ "هَوُسَ", "Hausa (Ajami)" ] ]
	nY = 170
	for i = 1 to len(aW)
		cT = aW[i][1]
		cS = aW[i][2]
		nX = 60 + ((i - 1) % 3) * 440
		nYY = nY + floor((i - 1) / 3) * 250
		oC.AddRoundRectQ(nX, nYY, 400, 200, 14).FillQ("#FFFFFF").Stroke("#E6DAC4", 1.5)
		oC.Flush()
		oC.SetFontQ(BOLD, 56).AddTextQ(cT, nX + 24, nYY + 88).Fill(PURPLE)
		oC.Flush()
		cFacts = cS + " · " + Q(cT).NumberOfChars() + " chars · " + len(cT) + " bytes · " + Q(cT).Script()
		oC.SetFontQ(FONT, 18).AddTextQ(cFacts, nX + 24, nYY + 150).Fill(INK2)
		oC.Flush()
	next
	Mark(oC, nW, nH)
	oC.ToPNGHiRes("string.png")
	Wrote("string.png")
catch
	? "ERR string: " + cCatchError
done

# ----------------------------------------------------------------- regex
try
	nW = 1400
	nH = 560
	oC = new stzCanvas(nW, nH)
	oC.SetBackground(PAPER)
	Title(oC, "A pattern, its matches, their places", "rx() finds them; the engine measures where each one sits in the line")
	cText = "RGPH 2012 counted 17138707 people in 8 regions; the 2026 site shows them."
	oRx = rx("\d+")
	oRx.MatchAnywhere(cText)
	aM = oRx.Matches()
	nX0 = 60
	nYB = 300
	nSize = 30
	# highlight every number: its x is the width of what precedes it
	nFrom = 1
	for i = 1 to len(aM)
		aPos = Q(cText).FindAll(aM[i])
		nAbs = 0
		for k = 1 to len(aPos)
			if aPos[k] >= nFrom and nAbs = 0
				nAbs = aPos[k]
			ok
		next
		if nAbs > 0
			cBefore = Q(cText).Section(1, nAbs - 1)
			nX = nX0 + FONT.WidthOf(cBefore, nSize)
			nWd = FONT.WidthOf(aM[i], nSize)
			oC.AddRoundRectQ(nX - 4, nYB - 34, nWd + 8, 46, 8).FillQ("#E9DDF5").Stroke(PURPLE, 1.5)
			oC.Flush()
			oC.SetFontQ(FONT, 15).AddTextQ("" + nAbs, nX, nYB + 36).Fill(PURPLE)
			oC.Flush()
			nFrom = nAbs + len(aM[i])
		ok
	next
	oC.SetFontQ(FONT, nSize).AddTextQ(cText, nX0, nYB).Fill(INK)
	oC.Flush()
	oC.SetFontQ(BOLD, 26).AddTextQ('rx("\d+").MatchAnywhere(text)', nX0, 190).Fill(PURPLE)
	oC.Flush()
	oC.SetFontQ(FONT, 22).AddTextQ("Matches(): " + @@(aM), nX0, 420).Fill(INK2)
	oC.Flush()
	Mark(oC, nW, nH)
	oC.ToPNGHiRes("regex.png")
	Wrote("regex.png")
catch
	? "ERR regex: " + cCatchError
done

# ----------------------------------------------------------- collections
try
	o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
	oD = new stzDiagram("pipeline")
	oD.AddNodeXTT(:a, @@(o1.Content()), [ :type = "box", :color = "#3E6EA8" ])
	oD.AddNodeXTT(:b, "DuplicatesRemoved()", [ :type = "hexagon", :color = PURPLE ])
	oD.AddNodeXTT(:c, @@(o1.DuplicatesRemoved()), [ :type = "box", :color = "#3E6EA8" ])
	oD.AddNodeXTT(:d, "Sorted()", [ :type = "hexagon", :color = PURPLE ])
	oD.AddNodeXTT(:e, @@(Q(o1.DuplicatesRemoved()).Sorted()), [ :type = "box", :color = "#3E6EA8" ])
	oD.AddNodeXTT(:f, "Reversed()", [ :type = "hexagon", :color = PURPLE ])
	oD.AddNodeXTT(:g, @@(Q(Q(o1.DuplicatesRemoved()).Sorted()).Reversed()), [ :type = "box", :color = GREEN ])
	oD.AddEdge(:a, :b)
	oD.AddEdge(:b, :c)
	oD.AddEdge(:c, :d)
	oD.AddEdge(:d, :e)
	oD.AddEdge(:e, :f)
	oD.AddEdge(:f, :g)
	oD.ToCanvasXT([ :Font = FONT, :NodeWidth = 300, :NodeHeight = 56, :FontSize = 18 ])
	oD.LastCanvas().ToPNG("collections.png")
	Wrote("collections.png")
catch
	? "ERR collections: " + cCatchError
done

# ---------------------------------------------------------------- tables
try
	aRows = [ [ "Agadez", 487620, 621917 ], [ "Diffa", 593821, 145832 ], [ "Dosso", 2037713, 31382 ],
	          [ "Maradi", 3402094, 39349 ], [ "Niamey", 1026848, 556 ], [ "Tahoua", 3328365, 107321 ],
	          [ "Tillaberi", 2722482, 90600 ], [ "Zinder", 3539764, 146662 ] ]
	nW = 1400
	nH = 820
	oC = new stzCanvas(nW, nH)
	oC.SetBackground(PAPER)
	Title(oC, "A table that knows its columns", "eight regions of Niger: people, square kilometres, and a density the engine computes per row")
	aCols = [ "Region", "People", "km²", "People / km²" ]
	aX = [ 80, 420, 720, 1020 ]
	nY = 170
	oC.AddRoundRectQ(60, nY - 36, 1280, 50, 10).FillQ("#EFE6F7").Stroke("#C9B3DE", 1)
	oC.Flush()
	for j = 1 to 4
		oC.SetFontQ(BOLD, 20).AddTextQ(aCols[j], aX[j], nY).Fill(PURPLE)
		oC.Flush()
	next
	for i = 1 to len(aRows)
		nYY = nY + 60 * i + 10
		if i % 2 = 0
			oC.AddRoundRectQ(60, nYY - 36, 1280, 50, 6).FillQ("#FFFFFF").Stroke("#FFFFFF00", 0)
			oC.Flush()
		ok
		oC.SetFontQ(BOLD, 22).AddTextQ(aRows[i][1], aX[1], nYY).Fill(INK)
		oC.Flush()
		oC.SetFontQ(FONT, 22).AddTextQ(StzFactNumText(aRows[i][2]), aX[2], nYY).Fill(INK2)
		oC.Flush()
		oC.SetFontQ(FONT, 22).AddTextQ(StzFactNumText(aRows[i][3]), aX[3], nYY).Fill(INK2)
		oC.Flush()
		nD = aRows[i][2] / aRows[i][3]
		cColor = INK2
		if nD > 100 cColor = RED ok
		oC.SetFontQ(BOLD, 22).AddTextQ(StzFactNumText(nD), aX[4], nYY).Fill(cColor)
		oC.Flush()
	next
	oC.SetFontQ(FONT, 18).AddTextQ("Source: RGPH 2012, Institut National de la Statistique du Niger; areas measured on WGS84 by the engine.", 62, nH - 60).Fill(INK2)
	oC.Flush()
	Mark(oC, nW, nH)
	oC.ToPNGHiRes("tables.png")
	Wrote("tables.png")
catch
	? "ERR tables: " + cCatchError
done

# ------------------------------------------------------------------ i18n
try
	nW = 1400
	nH = 700
	oC = new stzCanvas(nW, nH)
	oC.SetBackground(PAPER)
	Title(oC, "Languages name themselves", "StzLanguageQ(:X).NativeName() -- shaped by the engine, right to left where the script says so")
	aL = [ :Hausa, :Arabic, :French, :Russian, :Greek, :Hebrew, :Turkish, :Swahili, :Spanish ]
	for i = 1 to len(aL)
		cNative = StzLanguageQ(aL[i]).NativeName()
		cCode = StzLanguageQ(aL[i]).Abbreviation()
		nX = 60 + ((i - 1) % 3) * 440
		nYY = 150 + floor((i - 1) / 3) * 160
		oC.AddRoundRectQ(nX, nYY, 400, 130, 14).FillQ("#FFFFFF").Stroke("#E6DAC4", 1.5)
		oC.Flush()
		oC.SetFontQ(BOLD, 40).AddTextQ(cNative, nX + 24, nYY + 66).Fill(PURPLE)
		oC.Flush()
		oC.SetFontQ(FONT, 18).AddTextQ(StzLower("" + aL[i]) + " · " + cCode, nX + 24, nYY + 106).Fill(INK2)
		oC.Flush()
	next
	Mark(oC, nW, nH)
	oC.ToPNGHiRes("i18n.png")
	Wrote("i18n.png")
catch
	? "ERR i18n: " + cCatchError
done

# ------------------------------------------------------------------- nlp
try
	cS = "The running cats sat on the mats"
	aWords = Q(cS).Words()
	oD = new stzDiagram("lemmas")
	for i = 1 to len(aWords)
		cW = aWords[i]
		cL = Q(cW).Lemmatized()
		oD.AddNodeXTT("w" + i, cW, [ :type = "box", :color = "#3E6EA8" ])
		oD.AddNodeXTT("l" + i, cL, [ :type = "ellipse", :color = GREEN ])
		oD.AddEdgeXT("w" + i, "l" + i, "lemma")
	next
	oD.AddClusterXTT(:sent, "sentence: " + cS + "  (language: " + Q(cS).Language() + ", sentiment: " + Q(cS).Sentiment() + ")",
		[ "w1", "w2", "w3", "w4", "w5", "w6", "w7" ], "#EFE6F7")
	oD.ToCanvasXT([ :Font = FONT, :NodeWidth = 130, :NodeHeight = 50, :FontSize = 18 ])
	oD.LastCanvas().ToPNG("nlp.png")
	Wrote("nlp.png")
catch
	? "ERR nlp: " + cCatchError
done

# ---------------------------------------------------------------- agents
try
	oD = new stzDiagram("crossing")
	oD.AddNodeXTT(:agent, "agent (LLM)", [ :type = "ellipse", :color = "#7A5A9E" ])
	oD.AddNodeXTT(:bench, "workbench (virtual twin)", [ :type = "folder", :color = "#3E6EA8" ])
	oD.AddNodeXTT(:plan, "update plan (610 ops)", [ :type = "note", :color = "#9E8C4E" ])
	oD.AddNodeXTT(:court, "court: scope · capability · governance", [ :type = "hexagon", :color = "#B4462F" ])
	oD.AddNodeXTT(:actor, "governed actor (human)", [ :type = "box", :color = GREEN ])
	oD.AddNodeXTT(:real, "reality", [ :type = "cylinder", :color = "#8C5A4E" ])
	oD.AddEdgeXT(:agent, :bench, "rehearses")
	oD.AddEdgeXT(:bench, :plan, "exports")
	oD.AddEdgeXT(:plan, :court, "faces")
	oD.AddEdgeXT(:court, :actor, "admits")
	oD.AddEdgeXT(:actor, :real, "commits")
	oD.AddEdgeXT(:agent, :court, "cannot commit: no effectful capability")
	oD.AddClusterXTT(:safe, "the safe world: no reference to reality", [ :agent, :bench, :plan ], "#EFE6F7")
	oD.ToCanvasXT([ :Font = FONT, :NodeWidth = 230, :NodeHeight = 60, :FontSize = 18 ])
	oD.LastCanvas().ToPNG("agents.png")
	Wrote("agents.png")
catch
	? "ERR agents: " + cCatchError
done

# ----------------------------------------------------------------- stats
try
	oH = new stzHistogram([ 12,15,18,22,23,25,26,27,28,30,31,33,35,38,41,45,52,58,61,70, 24, 29, 32, 36, 40 ])
	oH.ToPNG("stats.png", [ :Font = FONT ])
	Wrote("stats.png")
catch
	? "ERR stats: " + cCatchError
done

# ---------------------------------------------------------------- system
try
	oD = new stzDiagram("twin")
	oD.AddNodeXTT(:disk, "disk: project/", [ :type = "cylinder", :color = "#8C5A4E" ])
	oD.AddNodeXTT(:d1, "course.zknw", [ :type = "note", :color = "#9E8C4E" ])
	oD.AddNodeXTT(:d2, "chapters/ (60 files)", [ :type = "folder", :color = "#3E6EA8" ])
	oD.AddNodeXTT(:twin, "virtual twin", [ :type = "cylinder", :color = PURPLE ])
	oD.AddNodeXTT(:t1, "course.zknw (deleted)", [ :type = "note", :color = "#B4462F" ])
	oD.AddNodeXTT(:t2, "chapters/ (deleted)", [ :type = "folder", :color = "#B4462F" ])
	oD.AddNodeXTT(:plan, "update plan: 61 deletions, 0 committed", [ :type = "box", :color = GREEN ])
	oD.AddEdge(:disk, :d1)
	oD.AddEdge(:disk, :d2)
	oD.AddEdge(:twin, :t1)
	oD.AddEdge(:twin, :t2)
	oD.AddEdgeXT(:disk, :twin, "ReadThrough")
	oD.AddEdgeXT(:twin, :plan, "GenerateUpdatePlan()")
	oD.AddClusterXTT(:real, "reality (untouched)", [ :disk, :d1, :d2 ], "#E4F1EA")
	oD.AddClusterXTT(:safe, "workbench (rehearsal)", [ :twin, :t1, :t2 ], "#EFE6F7")
	oD.ToCanvasXT([ :Font = FONT, :NodeWidth = 240, :NodeHeight = 56, :FontSize = 18 ])
	oD.LastCanvas().ToPNG("system.png")
	Wrote("system.png")
catch
	? "ERR system: " + cCatchError
done

# ------------------------------------------------------------------- web
try
	oD = new stzDiagram("request")
	oD.SetNotation(StzUmlSequenceNotation())
	oD.AddNodeXTT("c", "Client", [ :type = "actor" ])
	oD.AddNodeXTT("s", ":AppServer", [ :type = "participant" ])
	oD.AddNodeXTT("a", ":Auth", [ :type = "participant" ])
	oD.AddNodeXTT("l", ":SLA", [ :type = "participant" ])
	oD.AddEdgeXT("c", "s", "POST /login")
	oD.AddEdgeXT("s", "a", "Login(user, pass)")
	oD.AddEdgeXT("a", "s", "token")
	oD.AddEdgeXT("s", "l", "http.request.ms = 12")
	oD.AddEdgeXT("l", "s", "within budget")
	oD.AddEdgeXT("s", "c", "200 OK")
	oD.ToCanvasXT([ :Font = FONT, :NodeWidth = 150, :NodeHeight = 52, :FontSize = 16 ])
	oD.LastCanvas().ToPNG("web.png")
	Wrote("web.png")
catch
	? "ERR web: " + cCatchError
done

# ------------------------------------------------------------------ meta
try
	oD = new stzDiagram("gate")
	oD.AddNodeXTT(:gate, "ONE rule gate: stzRuleReport.Ingest()", [ :type = "hexagon", :color = PURPLE ])
	aDom = [ "code", "graph", "org", "security", "service", "agentic", "diagram", "data", "perf", "education", "workflow" ]
	for i = 1 to len(aDom)
		oD.AddNodeXTT("d" + i, aDom[i] + " rules", [ :type = "box", :color = "#3E6EA8" ])
		oD.AddEdge("d" + i, :gate)
	next
	oD.AddNodeXTT(:report, "[ :rule, :subject, :where, :severity, :message ]", [ :type = "note", :color = "#9E8C4E" ])
	oD.AddNodeXTT(:verdict, "verdict: 0 findings", [ :type = "doublecircle", :color = GREEN ])
	oD.AddEdge(:gate, :report)
	oD.AddEdge(:report, :verdict)
	oD.ToCanvasXT([ :Font = FONT, :NodeWidth = 190, :NodeHeight = 52, :FontSize = 16 ])
	oD.LastCanvas().ToPNG("meta.png")
	Wrote("meta.png")
catch
	? "ERR meta: " + cCatchError
done

# ----------------------------------------------------------------- files
try
	oD = new stzDiagram("json")
	oD.AddNodeXTT(:root, "{ document }", [ :type = "folder", :color = PURPLE ])
	oD.AddNodeXTT(:n, '"name": "Softanza"', [ :type = "box", :color = "#3E6EA8" ])
	oD.AddNodeXTT(:l, '"langs": [ ... ]', [ :type = "folder", :color = "#3E6EA8" ])
	oD.AddNodeXTT(:l1, '"en"', [ :type = "box", :color = GREEN ])
	oD.AddNodeXTT(:l2, '"fr"', [ :type = "box", :color = GREEN ])
	oD.AddNodeXTT(:l3, '"ar"', [ :type = "box", :color = GREEN ])
	oD.AddNodeXTT(:l4, '"ha"', [ :type = "box", :color = GREEN ])
	oD.AddNodeXTT(:x, "XML: XXE closed by construction", [ :type = "note", :color = "#B4462F" ])
	oD.AddNodeXTT(:z, "zip only · UTF-8 · 64 MB cap", [ :type = "note", :color = "#9E8C4E" ])
	oD.AddEdge(:root, :n)
	oD.AddEdge(:root, :l)
	oD.AddEdge(:l, :l1)
	oD.AddEdge(:l, :l2)
	oD.AddEdge(:l, :l3)
	oD.AddEdge(:l, :l4)
	oD.AddEdge(:root, :x)
	oD.AddEdge(:root, :z)
	oD.ToCanvasXT([ :Font = FONT, :NodeWidth = 200, :NodeHeight = 52, :FontSize = 16 ])
	oD.LastCanvas().ToPNG("files.png")
	Wrote("files.png")
catch
	? "ERR files: " + cCatchError
done

# --------------------------------------------------------- extensibility
try
	oD = new stzDiagram("door")
	oD.AddNodeXTT(:engine, "Softanza engine (Zig)", [ :type = "component", :color = PURPLE ])
	oD.AddNodeXTT(:door, "the external door: one posture per call", [ :type = "hexagon", :color = "#B4462F" ])
	oD.AddNodeXTT(:py, "Python", [ :type = "component", :color = "#3E6EA8" ])
	oD.AddNodeXTT(:js, "JavaScript", [ :type = "component", :color = "#3E6EA8" ])
	oD.AddNodeXTT(:jl, "Julia", [ :type = "component", :color = "#3E6EA8" ])
	oD.AddNodeXTT(:pl, "Prolog", [ :type = "component", :color = "#3E6EA8" ])
	oD.AddNodeXTT(:c, "C libraries (vendored, pinned)", [ :type = "component", :color = "#8C5A4E" ])
	oD.AddEdgeXT(:engine, :door, "governed")
	oD.AddEdge(:door, :py)
	oD.AddEdge(:door, :js)
	oD.AddEdge(:door, :jl)
	oD.AddEdge(:door, :pl)
	oD.AddEdgeXT(:engine, :c, "links")
	oD.ToCanvasXT([ :Font = FONT, :NodeWidth = 230, :NodeHeight = 56, :FontSize = 17 ])
	oD.LastCanvas().ToPNG("extensibility.png")
	Wrote("extensibility.png")
catch
	? "ERR extensibility: " + cCatchError
done

# ----------------------------------------------------------------- sound
try
	oD = new stzDiagram("audio")
	oD.AddNodeXTT(:src, "oscillator 440 Hz", [ :type = "ellipse", :color = "#3E6EA8" ])
	oD.AddNodeXTT(:env, "envelope", [ :type = "box", :color = "#3E6EA8" ])
	oD.AddNodeXTT(:flt, "low-pass filter", [ :type = "box", :color = "#3E6EA8" ])
	oD.AddNodeXTT(:mix, "mixer", [ :type = "hexagon", :color = PURPLE ])
	oD.AddNodeXTT(:sink, "device sink (lock-free callback)", [ :type = "cylinder", :color = GREEN ])
	oD.AddNodeXTT(:ana, "analysis: pitch · onsets · spectrogram", [ :type = "note", :color = "#9E8C4E" ])
	oD.AddEdge(:src, :env)
	oD.AddEdge(:env, :flt)
	oD.AddEdge(:flt, :mix)
	oD.AddEdge(:mix, :sink)
	oD.AddEdge(:mix, :ana)
	oD.AddClusterXTT(:graph, "the owned sound graph: no allocation, no lock in the callback", [ :src, :env, :flt, :mix ], "#EFE6F7")
	oD.ToCanvasXT([ :Font = FONT, :NodeWidth = 250, :NodeHeight = 56, :FontSize = 17 ])
	oD.LastCanvas().ToPNG("sound.png")
	Wrote("sound.png")
catch
	? "ERR sound: " + cCatchError
done

# --------------------------------------------------------- documentation
try
	oD = new stzDiagram("docs")
	oD.AddNodeXTT(:nar, "narration (.md with code cells)", [ :type = "note", :color = "#9E8C4E" ])
	oD.AddNodeXTT(:run, "every cell RUNS", [ :type = "hexagon", :color = PURPLE ])
	oD.AddNodeXTT(:out, "outputs never stored", [ :type = "box", :color = "#B4462F" ])
	oD.AddNodeXTT(:page, "the page the reader sees", [ :type = "box", :color = GREEN ])
	oD.AddNodeXTT(:ask, "Ask() · HowTo() · ExplainMethod()", [ :type = "ellipse", :color = "#3E6EA8" ])
	oD.AddNodeXTT(:lib, "the library documents itself", [ :type = "cylinder", :color = "#3E6EA8" ])
	oD.AddEdge(:nar, :run)
	oD.AddEdge(:run, :out)
	oD.AddEdge(:run, :page)
	oD.AddEdge(:lib, :ask)
	oD.AddEdge(:ask, :page)
	oD.ToCanvasXT([ :Font = FONT, :NodeWidth = 250, :NodeHeight = 56, :FontSize = 17 ])
	oD.LastCanvas().ToPNG("documentation.png")
	Wrote("documentation.png")
catch
	? "ERR documentation: " + cCatchError
done

# ----------------------------------------------------------- concurrency
try
	oD = new stzDiagram("fleet")
	oD.AddNodeXTT(:sup, "supervisor", [ :type = "hexagon", :color = PURPLE ])
	for i = 1 to 6
		oD.AddNodeXTT("w" + i, "worker " + i, [ :type = "box", :color = "#3E6EA8" ])
		oD.AddEdgeXT(:sup, "w" + i, "ticks")
	next
	oD.AddNodeXTT(:dead, "worker 7 (restarted)", [ :type = "box", :color = "#B4462F" ])
	oD.AddEdgeXT(:sup, :dead, "state-proof: restart")
	oD.AddNodeXTT(:ring, "reactor: no callback into the VM", [ :type = "note", :color = "#9E8C4E" ])
	oD.AddEdge(:sup, :ring)
	oD.AddClusterXTT(:node, "one node, 12 cores", [ "w1", "w2", "w3", "w4", "w5", "w6", :dead ], "#E4F1EA")
	oD.ToCanvasXT([ :Font = FONT, :NodeWidth = 190, :NodeHeight = 52, :FontSize = 17 ])
	oD.LastCanvas().ToPNG("concurrency.png")
	Wrote("concurrency.png")
catch
	? "ERR concurrency: " + cCatchError
done

# ---------------------------------------------------------------- numeric
try
	aPts = []
	for i = 0 to 40
		x = i / 4
		aPts + [ x, x * x ]
	next
	oS = StzPlotQ(:Scatter, aPts)
	oS.ToPNG("numeric.png", [ :Font = FONT ])
	Wrote("numeric.png")
catch
	? "ERR numeric: " + cCatchError
done

? "DONE"

# --- helpers: all at the bottom would be the Ring rule; these are tiny ---
func Title(oC, cT, cS)
	oC.SetFontQ(BOLD, 34).AddTextQ(cT, 50, 64).Fill(INK)
	oC.Flush()
	oC.SetFontQ(FONT, 18).AddTextQ(cS, 52, 94).Fill(INK2)
	oC.Flush()

func Mark(oC, nW, nH)
	oC.SetFontQ(BOLD, 16).AddTextQ("made with Softanza", nW - 200, nH - 30).Fill(PURPLE)
	oC.Flush()

func Wrote(cName)
	? "OK  " + cName

func Diag(oD, cFile)
	oD.ToCanvasXT(OPT)
	oD.LastCanvas().ToPNG(cFile)
	Wrote(cFile)

