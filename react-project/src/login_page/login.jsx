import { useState } from "react";
import { useNavigate } from "react-router-dom"


function Login() {

    const[username,setUsername]=useState("");
    const[password,setPassword]=useState("");

    const navigate = useNavigate();

    function handleUsernameChange(e){
        setUsername(e.target.value);
    }
    function handlePasswordChange(e){
        setPassword(e.target.value);
    }
    async function handleSubmit(e){
        e.preventDefault();
        alert("username:"+ username + "/nPassword:" +password)


        const response= await fetch("http://127.0.0.1:8000/login",{
            method: "POST",
            headers:{
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                username: username,
                password: password,
            }),
        });
        const data = await response.json();
        console.log(data);

        if (data.token){
            localStorage.setItem("token",data.token);

            navigate("/predict");
        }else{
            alert("Invalid");
        }
    }
    
    return (
    <div className="title">
        <h1>Welcome to MaribenPredict</h1>   

        <div className="login">
            
            <h3>Login</h3><br></br>

            <form onSubmit={handleSubmit}>
                <div className="input-box">
                    <input 
                    type="text" 
                    value={username} 
                    onChange={handleUsernameChange} 
                    placeholder="Username" 
                    />       
                </div>

                <div className="input-box">
                    <input 
                    type="text" 
                    value={password}
                    onChange={handlePasswordChange}
                    placeholder="Password"
                     />          
                </div><br></br>

                <div className="submit-button">
                    <button type="submit">Login</button>
                </div>
            </form>
        </div>
    </div>        
    )    
}
export default Login;