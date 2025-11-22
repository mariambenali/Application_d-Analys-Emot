import {useState }from "react";
import'./Dashboard.css'


function Dashboard(){
    const[prediction, setPrediction]= useState("");
    const[message ,setMessage] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch("http://127.0.0.1:8000/predict",{
            method: "POST",
            headers: { "Content-Type" : "application/json" },
            body: JSON.stringify({text: message})
        });
        const data = await response.json();
        setPrediction(data.var); 

        setMessage("");
        setTimeout(() => setPrediction(""), 3000);

        
    };

    return(
        <div className="prediction">
            <form onSubmit={handleSubmit}>
                <input
                   type="text" 
                   placeholder="Put your message here!"
                   value={message}
                   onChange={(e) => setMessage(e.target.value)}
                />
                <button type="submit">Predict</button>
            </form>
            {prediction && (
                <h3 className={`bounce`}>
                    Emotion detected: {prediction} 
                </h3>
            )} 
        </div>
    );
}

export default Dashboard;