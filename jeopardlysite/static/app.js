function App(props) {
  const [ gameData, setGameData ] = React.useState(null)
  const [ status, setStatus ] = React.useState(null)

  async function startGame() {
    setGameData(null)
    setStatus("Fetching clues...")

    await fetch('/jeopardly/etl')

    setStatus("Loading game...")

    fetch('/jeopardly/game-data')
      .then(response => response.json())
      .then((gd) => {
        setGameData(gd)
        setStatus(null)
      })
  }


  return <div>
    <h1>Jeopard.ly</h1>
    <h4>The quiz app with a name that just <em>feels</em> weird to say</h4>

    <div className="buttons">
      <button type="button" onClick={() => {startGame()}}>
        Start New Game
      </button>
    </div>
    {status && <p className="status">{status}</p>}
    {gameData && <GameBoard categories={gameData} />}
  </div>  
}

function GameBoard({categories}) {
  return <div className="game-board">
    {categories.map((category, catIdx) => {

      const firstFiveClues = category.clues.slice(0, 5)
      
      return <div className="col" key={catIdx}>
        <div className="category-title">{category.title}</div>
        {firstFiveClues.map((clue, clueIdx) => {
          return <Tile clue={clue} />
        })}
      </div>
    })}
  </div>
}

function Tile({clue}) {

  function getDisplay() {
    if (clicks === 0) {
      return clue.value || "???"
    } else if (clicks === 1) {
      return clue.prompt
    } else if (clicks === 2) {
      return clue.solution
    } else {
      return ""
    }
  }

  function getTileClass() {
    let tileClass = "clue "
    if (clicks === 0) {
      tileClass += "number"
    } else if (clicks > 2) {
      tileClass += "done"
    }
    return tileClass
  }

  const [ clicks, setClicks ] = React.useState(0)
  
  return <div className={getTileClass()} onClick={() => setClicks(clicks + 1)}>
    {getDisplay()}
  </div>
}