import React, { useState, useEffect } from 'react';
import { Container, Typography, Box, Paper, CircularProgress, Alert } from '@mui/material';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
import { Bar } from 'react-chartjs-2';
import axios from 'axios';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const Home = () => {
  const [matchesByYear, setMatchesByYear] = useState([]);
  const [winsByTeam, setWinsByTeam] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const [matchesRes, winsRes] = await Promise.all([
          axios.get('http://localhost:8000/api/matches_per_year/'),
          axios.get('http://localhost:8000/api/matches_won_per_team/')
        ]);
        setMatchesByYear(matchesRes.data);
        setWinsByTeam(winsRes.data);
        setError(null);
      } catch (err) {
        setError('Could not fetch IPL data. Is backend running?');
      } finally {
        setLoading(false);
      }
    };

    fetchStats();
  }, []);

  if (loading) {
    return (
      <Container sx={{ mt: 6, display: 'flex', justifyContent: 'center' }}>
        <CircularProgress />
      </Container>
    );
  }

  if (error) {
    return (
      <Container sx={{ mt: 6 }}>
        <Alert severity="error">{error}</Alert>
      </Container>
    );
  }

  // Matches per year chart
  const matchesChart = {
    labels: matchesByYear.map(item => item.season),
    datasets: [
      {
        label: 'Matches Played',
        data: matchesByYear.map(item => item.count),
        backgroundColor: 'rgba(255, 159, 64, 0.6)',
        borderColor: 'rgba(255, 159, 64, 0.6)',
        borderWidth: 1,
      },
    ],
  };

  // Matches won per team chart (all bars same color)
  const winsChart = {
    labels: winsByTeam.map(item => item.winner),
    datasets: [
      {
        label: 'Matches Won',
        data: winsByTeam.map(item => item.count),
        backgroundColor: 'rgba(175, 223, 87, 0.6)', 
        borderColor: 'rgba(175, 223, 87, 0.6)', 
        borderWidth: 1,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: false },
    },
    scales: {
      y: { beginAtZero: true },
    },
  };

  return (
    <Container sx={{ mt: 4 }}>
      <Typography variant="h4" align="center" gutterBottom>
        IPL Dashboard
      </Typography>

      <Box sx={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
        <Paper sx={{ p: 3 }}>
          <Typography variant="h5" gutterBottom>
            Matches Played Per Year
          </Typography>
          <Box sx={{ height: 400 }}>
            <Bar data={matchesChart} options={chartOptions} />
          </Box>
        </Paper>

        <Paper sx={{ p: 3 }}>
          <Typography variant="h5" gutterBottom>
            Matches Won Per Team
          </Typography>
          <Box sx={{ height: 500 }}>
            <Bar data={winsChart} options={chartOptions} />
          </Box>
        </Paper>
      </Box>
    </Container>
  );
};

export default Home;

