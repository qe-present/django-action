import { createBrowserRouter } from "react-router"
import MainLayout from "@/components/MainLayout.tsx"
import Home from "@/views/Home"

const routes = createBrowserRouter([
  {
    path: "/",
    element: <MainLayout />,
    children: [{ index: true, element: <Home /> }],
  },
])
export default routes
