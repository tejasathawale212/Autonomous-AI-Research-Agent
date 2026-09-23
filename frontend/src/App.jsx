import { useState } from "react"
import ReactMarkdown from "react-markdown"


function App() {
  const [question, setQuestion] = useState("")
  const [loading, setLoading] = useState(false)

  const [researchStarted, setResearchStarted] = useState(false)

  const [result, setResult] = useState("")

  const [error, setError] = useState("")

  const [sources, setSources] = useState([])


  const [researchComplete, setResearchComplete] = useState(false)

  const handleResearch = async () => {
    if (!question.trim()) return

    setLoading(true)
    setResearchStarted(true)
    setResearchComplete(false)
    setError("")
    setResult("")
    setSources([])

    try {
      const response = await fetch("http://127.0.0.1:8000/research", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
        }),
      })

      if (!response.ok) {
        throw new Error(`Research request failed: ${response.status}`)
      }

      const data = await response.json()

      setResult(data.result)
      setSources(data.sources)
      setResearchComplete(true)
    } catch (error) {
      console.error("Research failed:", error)
      setError(error.message)
    } finally {
      setLoading(false)
    }
  }
  const handleNewResearch = () => {
    setResearchComplete(false)
    setQuestion("")
    setResult("")
    setError("")
    setResearchStarted(false)
    setProgress({
      question_validator: false,
      planner: false,
      searcher: false,
      extractor: false,
      ingestor: false,
      retriever: false,
      evaluator: false,
      synthesizer: false,
    })
  }

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      {/* Header */}
      <header className="border-b border-slate-800">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-5">
          <div>
            <h1 className="text-xl font-semibold">
              Autonomous Research Agent
            </h1>
            <p className="text-sm text-slate-400">
              Evidence-backed AI research
            </p>
          </div>

          <div className="flex items-center gap-3">
            <div className="h-2 w-2 rounded-full bg-emerald-400" />
            <span className="text-sm text-slate-400">System ready</span>
          </div>
        </div>
      </header>

      <main className="mx-auto max-w-7xl px-6 py-12">
        {/* Research Input */}
        <section className="mx-auto max-w-4xl text-center">
          <p className="mb-4 text-sm font-medium tracking-widest text-blue-400">
            AUTONOMOUS AI RESEARCH
          </p>

          <h2 className="text-4xl font-bold tracking-tight sm:text-5xl">
            Research anything.
            <br />
            Get evidence-backed answers.
          </h2>

          <p className="mx-auto mt-5 max-w-2xl text-lg leading-8 text-slate-400">
            The agent searches the web, gathers evidence, evaluates sources,
            and synthesizes a research report.
          </p>

          <div className="mt-10 overflow-hidden rounded-2xl border border-slate-800 bg-slate-900 text-left shadow-2xl">
            <textarea
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder="What would you like to research?"
              className="min-h-36 w-full resize-none bg-transparent p-5 text-lg text-white outline-none placeholder:text-slate-600"
            />

            <div className="flex items-center justify-between border-t border-slate-800 px-5 py-4">
              <span className="text-sm text-slate-500">
                Ask a research question
              </span>

              <button
                onClick={handleResearch}
                disabled={loading || !question.trim()}
                className="rounded-xl bg-blue-600 px-6 py-3 font-medium transition hover:bg-blue-500 disabled:cursor-not-allowed disabled:opacity-50"
              >
                {loading ? "Researching..." : "Start Research"}
              </button>
            </div>
          </div>
        </section>

        {/* Research Workspace */}
        <section className="mt-16 grid gap-6 lg:grid-cols-[280px_1fr]">
          {/* Progress */}
          <aside className="rounded-2xl border border-slate-800 bg-slate-900 p-5">
            <div className="mb-6">
              <div>
                <h3 className="font-semibold">Research Report</h3>

                {researchStarted && (
                  <p className="mt-2 text-sm text-slate-400">
                    Researching: <span className="text-slate-300">{question}</span>
                  </p>
                )}

                <p className="mt-1 text-sm text-slate-500">
                  Evidence-backed synthesis
                </p>
              </div>
              <p className="mt-1 text-sm text-slate-500">
                Agent activity
              </p>
            </div>

            <div className="space-y-5">
              <ResearchStep
                label="Research started"
                done={researchStarted}
              />

              <ResearchStep
                label="Research report generated"
                done={researchComplete}
              />

              <ResearchStep
                label="Sources collected"
                done={researchComplete}
              />
            </div>
          </aside>

          {/* Report */}
          <section className="rounded-2xl border border-slate-800 bg-slate-900">
            <div className="border-b border-slate-800 px-6 py-5">
              <div className="flex items-center justify-between">
                <div>
                  <h3 className="font-semibold">Research Report</h3>
                  <p className="mt-1 text-sm text-slate-500">
                    Evidence-backed synthesis
                  </p>
                </div>

                <div className="flex items-center gap-3">
                  {researchStarted && !loading && (
                    <button
                      onClick={handleNewResearch}
                      className="rounded-lg border border-slate-700 px-3 py-1.5 text-xs text-slate-300 transition hover:border-slate-600 hover:bg-slate-800"
                    >
                      New Research
                    </button>
                  )}

                  <span className="rounded-full border border-blue-900 bg-blue-950 px-3 py-1 text-xs text-blue-300">
                    {loading
                      ? "Researching"
                      : researchComplete
                        ? "Research complete"
                        : researchStarted
                          ? "Research in progress"
                          : "Ready"}
                  </span>
                </div>
              </div>
            </div>

            <div className="min-h-80 p-6">
              {error && (
                <div className="mb-6 rounded-xl border border-red-900 bg-red-950/40 p-4 text-sm text-red-300">
                  Research failed: {error}
                </div>
              )}
              {result ? (
                <div className="prose prose-invert max-w-none">
                  <ReactMarkdown
                    components={{
                      a: ({ node, ...props }) => (
                        <a
                          {...props}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-blue-400 hover:text-blue-300 underline"
                        />
                      ),
                    }}
                  >
                    {result}
                  </ReactMarkdown>
                </div>
              ) : (
                <div className="space-y-4 text-slate-300">
                  <div className="h-4 w-3/4 animate-pulse rounded bg-slate-800" />
                  <div className="h-4 w-full animate-pulse rounded bg-slate-800" />
                  <div className="h-4 w-5/6 animate-pulse rounded bg-slate-800" />
                  <div className="h-4 w-2/3 animate-pulse rounded bg-slate-800" />
                </div>
              )}
            </div>

            {sources.length > 0 && (
              <div className="border-t border-slate-800 p-6">
                <h3 className="mb-4 font-semibold">Research Sources</h3>

                <div className="space-y-3">
                  {sources.map((source, index) => (
                    <a
                      key={source.url}
                      href={source.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="block rounded-xl border border-slate-800 bg-slate-950 p-4 transition hover:border-slate-700 hover:bg-slate-900"
                    >
                      <div className="flex gap-3">
                        <span className="text-sm text-slate-500">
                          {index + 1}
                        </span>

                        <div>
                          <p className="font-medium text-slate-300">
                            {source.title}
                          </p>

                          <p className="mt-1 text-xs text-slate-500">
                            {source.url}
                          </p>
                        </div>
                      </div>
                    </a>
                  ))}
                </div>
              </div>
            )}

          </section>
        </section>
      </main>
    </div>
  )
}

function ResearchStep({ label, done, active }) {
  return (
    <div className="flex items-center gap-3">
      <div
        className={`flex h-7 w-7 items-center justify-center rounded-full text-xs ${
          done
            ? "bg-emerald-500/20 text-emerald-400"
            : active
              ? "bg-blue-500/20 text-blue-400"
              : "bg-slate-800 text-slate-500"
        }`}
      >
        {done ? "✓" : active ? "•" : ""}
      </div>

      <span
        className={`text-sm ${
          done || active ? "text-slate-300" : "text-slate-600"
        }`}
      >
        {label}
      </span>
    </div>
  )
}

export default App