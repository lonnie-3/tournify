import axios from "axios"

function App() {
  message = axios.get('http://localhost:8000/')
  console.log(message)
  return (
    <div className="bg-red-500">Name is Addonay</div>
  )
}

export default App
