import { useState, useEffect } from 'react';
import api from '../api/axios';

export const usePatients = () => {
    const [patients, setPatients] = useState([]);
    const [loading, setLoading] = useState(true);

    const fetchPatients = async () => {
        try {
            const response = await api.get('/pacientes/');
            setPatients(response.data);
        } catch (error) {
            console.error("Error cargando pacientes:", error);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchPatients();
    }, []);

    return { patients, loading, refetch: fetchPatients };
};