import React, { useState, useEffect } from "react";
import axios from "axios";
import ReactDOM from "react-dom/client";
import "./index.css";

function CreateMovieGUI() {
  const [title, setTitle] = useState("");
  const [genre, setGenre] = useState("");
  const [scriptId, setScriptId] = useState("");
  const [producerId, setProducerId] = useState("");
  const [actorIds, setActorIds] = useState([]);
  const [effectIds, setEffectIds] = useState([]);
  const [scandalIds, setScandalIds] = useState([]);
  const [response, setResponse] = useState(null);

  const [scripts, setScripts] = useState([]);
  const [producers, setProducers] = useState([]);
  const [actors, setActors] = useState([]);
  const [effects, setEffects] = useState([]);
  const [scandals, setScandals] = useState([]);

useEffect(() => {
  axios.get("/scripts").then(res => setScripts(res.data));
  axios.get("/producers").then(res => setProducers(res.data));
  axios.get("/actors").then(res => setActors(res.data));
  axios.get("/effects").then(res => setEffects(res.data));
  axios.get("/scandals").then(res => setScandals(res.data));
}, []);

const handleSubmit = async () => {
  try {
    const payload = {
      title,
      genre,
      script_id: parseInt(scriptId),
      producer_id: parseInt(producerId),
      actor_ids: actorIds.map(Number),
      effect_ids: effectIds.map(Number),
      scandal_ids: scandalIds.map(Number),
    };
    const res = await axios.post("/movies/create/", payload);
    setResponse(res.data);
  } catch (err) {
    setResponse({ error: err.response?.data?.detail || "Error"});
  }
};

 return (
   <div className="p-4 max-w-3xl mx-auto font-sans">
     <h2 className="text=2xl font-bold mb-4">Create a Movie</h2>

     <input placeholder="Title" className="border p-2 w-full mb-2" value={title} onChange={e => setTitle(e.target.value)} />
     <input placeholder="Genre" className="border p-2 w-full mb-2" value={genre} onChange={e => setGenre(e.target.value)} />

     <select className="border p-2 w-full mb-2" value={scriptId} onChange={e => setScriptId(e.target.value)}>
       <option value="">Select Script</option>
       {scripts.map(script => (
         <option key={script.script_id} value={script.script_id}>{script.title}</option>
       ))}
     </select>

     <select className="border p-2 w-full mb-2" value={producerId} onChange={e => setProducerId(e.target.value)}>
       <option value="">Select Producer</option>
       {producers.map(p => (
         <option key={p.producer_id} value={p.producer_id}>{p.name}</option>
       ))}
     </select>

     <label className="block font-bold mt-2">Select Actors</label>
     <select multiple className="border p-2 w-full mb-2" value={actorIds} onChange={e => setActorIds([...e.target.selectedOptions].map(o => o.value))}>
       {actors.map(a => (
         <option key={a.actor_id} value={a.actor_id}>{a.anme}</option>
       ))}
     </select>

     <label className="block font-bold mt-2">Select Effects</label>
     <select multiple className="border p-2 w-full mb-2" value={effectIds} onChange={e => setEffectIds([...e.target.selectedOptions.map(o => o.value))}>
       {effects.map(eff => (
         <option key={eff.effect_id} value={eff.effect_id}>{eff.type}</option>
       ))}
     </select>

     <label className="block font-bold mt-2">Select Scandals</label>
     <select multiple className="border p-2 w-full mb-2" value={scandalIds} onChange={e => setScandalIds([...e.target.selectedOptions].map(o => o.value))}>
       {scandals.map(s => (
         <option key={s.scandal_id} value={s.scandal_id}>{s.description}</option>
       ))}
     </select>

     <button className="bg-blue-500 text-white px-4 py-2 rounded" onClick={handleSubmit}>Create Movie</button>

     {response && (
       <div className="mt-4 p-2 border rounded bg-gray-100">
         <pre>{JSON.stringify(response, null, 2)}</pre>
       </div>
     )}
   </div>
 );
}  

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<CreateMovieGui />);  
