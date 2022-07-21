import axios from "axios";

export const getInfo = async () => 
    await axios.get("http://localhost:5000/");

export const sendVideo = async (data) => 
    await axios.post("http://localhost:5000", data);