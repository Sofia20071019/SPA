import { useState } from "react"
import { Form, Button, Container } from "react-bootstrap"
import { useNavigate } from "react-router-dom"
import api from "../services/api"

function Login(){
const navigate = useNavigate()
const [email,setEmail]=useState("")
const [password,setPassword]=useState("")

const handleSubmit = async (e) => {
  e.preventDefault()
    try {

        const res = await api.post("/login", {
        email,
        password
        })

        const { user, accessToken } = res.data

        // guardar sesión
        localStorage.setItem("user", JSON.stringify(user))
        localStorage.setItem("token", accessToken)

        // redirect por rol
        if (user.rol_id === 1) {
        navigate("/admin")
        } else if (user.rol_id === 2) {

        navigate("/dashboard");
        }

    } catch (error) {
        alert(
        error.response?.data?.message ||
        "Credenciales incorrectas"
        );
    }
    }

    return(
        <Container className="mt-5">
        <h2>Login</h2>
        <Form onSubmit={handleSubmit}>

        <Form.Group>
        <Form.Label>Email</Form.Label>
        <Form.Control
        type="email"
        value={email}
        onChange={(e)=>setEmail(e.target.value)}
        required
        />
        </Form.Group>

        <Form.Group className="mt-3">
        <Form.Label>Password</Form.Label>
        <Form.Control
        type="password"
        value={password}
        onChange={(e)=>setPassword(e.target.value)}
        required
        />
        </Form.Group>

        <Button className="mt-4" type="submit">
        Ingresar
        </Button>
        </Form>
        </Container>
    )
}

export default Login