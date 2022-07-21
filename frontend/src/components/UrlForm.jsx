import { useState, createRef } from "react"
import { FormLabel, Input, Button, Alert, AlertIcon, CloseButton, useDisclosure } from "@chakra-ui/react"

function UrlForm() {

    const [urlValid, setUrlValid] = useState(true)

    const uriInput = createRef()

    const sendURL = async data => {await fetch("http://localhost:5000/", {
        method: "POST",
        body: data
    })}

    const saveURL = e => {
        e.preventDefault()
        let inputData = uriInput.current.value
        inputData
            .includes("https://youtube.com/watch?v=") ||
            inputData.includes("https://www.youtube.com/watch?v=") ||
            inputData.includes("youtube.com/watch?v=") ? sendURL(inputData) : setUrlValid(false)
    }

    return (
        <div>
            <form onSubmit={saveURL}>
                <FormLabel>Video URL</FormLabel>
                <Input 
                    placeholder="URL del video de YouTube"
                    type={"text"}
                    ref={uriInput}
                />
                <Button 
                    type="submit"
                    colorScheme={"blue"}
                    my={3}
                >
                    Descargar
                </Button>
            </form>
        </div>
    )
}

export default UrlForm