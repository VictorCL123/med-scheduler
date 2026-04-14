import React from 'react';
import { usePatients } from '../hooks/usePatients';
import { User, RefreshCw } from 'lucide-react';

const PatientsList = () => {
    const { patients, loading, refetch } = usePatients();

    if (loading) return <div className="p-10 text-center">Cargando pacientes...</div>;

    return (
        <div className="p-6">
            <div className="flex justify-between items-center mb-6">
                <h1 className="text-2xl font-bold flex items-center gap-2">
                    <User className="text-blue-600" /> Lista de Pacientes
                </h1>
                <button
                    onClick={refetch}
                    className="p-2 hover:bg-gray-100 rounded-full transition-colors"
                >
                    <RefreshCw size={20} />
                </button>
            </div>

            <div className="overflow-x-auto shadow-md rounded-lg">
                <table className="w-full text-left bg-white">
                    <thead className="bg-gray-50 border-b">
                        <tr>
                            <th className="p-4 font-semibold">Nombre</th>
                            <th className="p-4 font-semibold">Email</th>
                            <th className="p-4 font-semibold">Fecha Nac.</th>
                        </tr>
                    </thead>
                    <tbody>
                        {patients.map((p) => (
                            <tr key={p.id} className="border-b hover:bg-gray-50">
                                <td className="p-4">{p.nombre}</td>
                                <td className="p-4 text-gray-600">{p.correo}</td>
                                <td className="p-4">{p.fecha_nacimiento}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default PatientsList;