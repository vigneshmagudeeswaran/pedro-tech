import "./App.css";
import Axios from "axios";
import { useEffect, useState } from "react";

function App() {
  const [name, setName] = useState("");
  const [age, setAge] = useState(null);

  const fetchData = () => {
    Axios.get(`https://api.agify.io/?name=${name}`).then((res) => {
      setAge(res.data);
    });
  };

  return (
    <div className="App">
      <input
        placeholder=" Ex. Pedro ..."
        onChange={(event) => setName(event.target.value)}
      ></input>
      <button onClick={fetchData}> Predict Age</button>
      <h1> Predicted Name: {age?.name}</h1>
      <h1> Predicted Age: {age?.age}</h1>
      <h1> Predicted count: {age?.count}</h1>
    </div>
  );
}

export default App;
