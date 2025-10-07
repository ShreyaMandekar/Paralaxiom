import React, { useState, useEffect } from 'react';
import { Container, Typography, Box, Paper, CircularProgress, Alert, Select, MenuItem, FormControl, InputLabel } from '@mui/material';
import { Bar } from 'react-chartjs-2';
import axios from 'axios';

const ExtraRuns = () => {
  const [years, setYears] = useState([]);
  const [year, setYear] = useState('');
  const [extraData, setExtraData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchYears = async () => {
      try {
        const res = await axios.get('http://localhost:8000/api/available_years/');
        setYears(res.data);
        setYear(res.data[0]);
      } catch {
        setError('Could not fetch available years.');
      }
    };
    fetchYears();
  }, []);

  useEffect(() => {
    if (!year) return;
    const fetchExtraRuns = async () => {
      try {
        setLoading(true);
        const res = await axios.get(`http://localhost:8000/api/extra_runs/${year}/`);
        setExtraData(res.data);
      } catch {
        setError('Could not fetch extra runs data.');
      } finally {
        setLoading(false);
      }
    };
    fetchExtraRuns();
  }, [year]);

  if (loading) return <Container sx={{ mt: 6, display: 'flex', justifyContent: 'center' }}><CircularProgress /></Container>;
  if (error) return <Container sx={{ mt: 6 }}><Alert severity="error">{error}</Alert></Container>;

  const chartData = {
    labels: extraData.map(item => item.bowling_team),
    datasets: [{
      label: `Extra Runs in ${year}`,
      data: extraData.map(item => item.extra),
      backgroundColor: 'rgba(255, 159, 64, 0.6)'
    }]
  };

  return (
    <Container sx={{ mt: 4 }}>
      <Typography variant="h4" align="center" gutterBottom>Extra Runs Dashboard</Typography>

      <FormControl sx={{ minWidth: 120, mb: 3 }}>
        <InputLabel>Year</InputLabel>
        <Select value={year} onChange={e => setYear(e.target.value)} label="Year">
          {years.map(y => <MenuItem key={y} value={y}>{y}</MenuItem>)}
        </Select>
      </FormControl>

      <Paper sx={{ p: 3 }}>
        <Box sx={{ height: 400 }}><Bar data={chartData} options={{ responsive: true, plugins: { legend: { position: 'top' }}, scales: { y: { beginAtZero: true }}}} /></Box>
      </Paper>
    </Container>
  );
};

export default ExtraRuns;

