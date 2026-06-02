import { AuthProvider } from "./auth";
import api from "./api";
import { useEffect, useState } from "react";

export default function App() {

    const [posts, setPosts] = useState([]);

    useEffect(() => {
        api.get("/posts").then(res => setPosts(res.data));
    }, []);

    return (
        <AuthProvider>
            <h1>MiniBlog</h1>

            {posts.map(p => (
                <div key={p.id}>
                    <h3>{p.title}</h3>
                    <p>{p.content}</p>
                </div>
            ))}
        </AuthProvider>
    );
}