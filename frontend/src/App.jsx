import PatientsList from './pages/PatientsList'

function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      {/* Barra de navegación simple */}
      <nav className="bg-blue-700 p-4 text-white shadow-md mb-8">
        <div className="container mx-auto flex justify-between items-center">
          <h1 className="font-bold text-xl tracking-tight">MedScheduler Pro</h1>
          <div className="text-sm bg-blue-800 px-3 py-1 rounded-full">
            Admin Panel
          </div>
        </div>
      </nav>

      {/* Contenido Principal */}
      <main className="container mx-auto px-4">
        <div className="bg-white rounded-xl shadow-sm border border-gray-200">
          <PatientsList />
        </div>
      </main>

      <footer className="mt-12 py-6 text-center text-gray-500 text-sm">
        &copy; 2026 MedScheduler System
      </footer>
    </div>
  )
}

export default App