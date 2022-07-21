import { Alert, AlertIcon, CloseButton, useDisclosure, Text } from '@chakra-ui/react'
import './public/css/App.css'
import VideoCard from './components/VideoCard'
import UrlForm from './components/UrlForm'

function App() {

  const {onClose} = useDisclosure({defaultIsOpen: true, isOpen: true})

  return (
    <div>
      <Text fontSize={"5xl"} textAlign={"center"} mb={"3"}>YutDownloader HTTP</Text>
      <Alert
        id='alert'
        status='info'
        textAlign={"center"}
        alignItems={"center"}
        mb={"3"}>
        <AlertIcon/>
        Recomendamos usar las descargas de esta web para uso personal o no lucrativo, muchas de estas pueden tener derechos de autor
        <CloseButton onClick={onClose}/>
      </Alert>
      <UrlForm/>
      <VideoCard/>
    </div>
  )
}

export default App
