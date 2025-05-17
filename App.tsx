import { useState } from 'react';
import { 
  AppBar, 
  Toolbar, 
  Typography, 
  Container, 
  Box, 
  Card, 
  CardContent, 
  CardHeader, 
  IconButton, 
  Drawer, 
  List, 
  ListItem,
  ListItemButton,
  ListItemIcon, 
  ListItemText, 
  Divider,
  Avatar,
  useTheme,
  useMediaQuery,
  Stack
} from '@mui/material';
import { 
  Menu as MenuIcon, 
  Dashboard as DashboardIcon, 
  ListAlt as ListAltIcon, 
  Add as AddIcon, 
  Settings as SettingsIcon, 
  Person as PersonIcon, 
  ExitToApp as ExitToAppIcon,
  Spa as SpaIcon
} from '@mui/icons-material';
import { 
  BarChart, 
  Bar, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  Legend, 
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  LineChart,
  Line,
  AreaChart,
  Area
} from 'recharts';

// Dados de exemplo para os gráficos
const conformidadeData = [
  { nome: 'Alface', dentroPadrao: 85, abaixoPadrao: 10, acimaPadrao: 5 },
  { nome: 'Tomate', dentroPadrao: 70, abaixoPadrao: 20, acimaPadrao: 10 },
  { nome: 'Cenoura', dentroPadrao: 90, abaixoPadrao: 5, acimaPadrao: 5 },
  { nome: 'Brócolis', dentroPadrao: 75, abaixoPadrao: 15, acimaPadrao: 10 },
  { nome: 'Couve', dentroPadrao: 80, abaixoPadrao: 12, acimaPadrao: 8 },
];

const tendenciaData = [
  { mes: 'Jan', conformidade: 78 },
  { mes: 'Fev', conformidade: 82 },
  { mes: 'Mar', conformidade: 85 },
  { mes: 'Abr', conformidade: 90 },
  { mes: 'Mai', conformidade: 88 },
  { mes: 'Jun', conformidade: 92 },
];

const solucaoData = [
  { nome: 'Hipoclorito', valor: 45 },
  { nome: 'Vinagre', valor: 30 },
  { nome: 'Bicarbonato', valor: 15 },
  { nome: 'Água', valor: 10 },
];

const COLORS = ['#2e7d32', '#ff8f00', '#d32f2f', '#1976d2'];

function App() {
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down('sm'));
  const [drawerOpen, setDrawerOpen] = useState(false);

  const toggleDrawer = () => {
    setDrawerOpen(!drawerOpen);
  };

  const drawerContent = (
    <Box sx={{ width: 250 }} role="presentation">
      <Box sx={{ p: 2, display: 'flex', alignItems: 'center', justifyContent: 'center', bgcolor: 'primary.main', color: 'white' }}>
        <SpaIcon sx={{ mr: 1 }} />
        <Typography variant="h6" component="div">
          Lógica do Sabor
        </Typography>
      </Box>
      <Divider />
      <List>
        <ListItem disablePadding>
          <ListItemButton selected>
            <ListItemIcon>
              <DashboardIcon color="primary" />
            </ListItemIcon>
            <ListItemText primary="Dashboard" />
          </ListItemButton>
        </ListItem>
        <ListItem disablePadding>
          <ListItemButton>
            <ListItemIcon>
              <ListAltIcon />
            </ListItemIcon>
            <ListItemText primary="Processos" />
          </ListItemButton>
        </ListItem>
        <ListItem disablePadding>
          <ListItemButton>
            <ListItemIcon>
              <AddIcon />
            </ListItemIcon>
            <ListItemText primary="Novo Processo" />
          </ListItemButton>
        </ListItem>
      </List>
      <Divider />
      <List>
        <ListItem disablePadding>
          <ListItemButton>
            <ListItemIcon>
              <SettingsIcon />
            </ListItemIcon>
            <ListItemText primary="Configurações" />
          </ListItemButton>
        </ListItem>
        <ListItem disablePadding>
          <ListItemButton>
            <ListItemIcon>
              <PersonIcon />
            </ListItemIcon>
            <ListItemText primary="Perfil" />
          </ListItemButton>
        </ListItem>
        <ListItem disablePadding>
          <ListItemButton>
            <ListItemIcon>
              <ExitToAppIcon />
            </ListItemIcon>
            <ListItemText primary="Sair" />
          </ListItemButton>
        </ListItem>
      </List>
    </Box>
  );

  // Renderização personalizada para o rótulo do gráfico de pizza
  const renderCustomizedLabel = () => {
    // Não renderizar rótulos no gráfico, apenas valores na legenda abaixo
    return null;
  };

  // Componente de legenda personalizada para o gráfico de pizza
  const renderCustomLegend = () => {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', flexWrap: 'wrap', mt: 2 }}>
        {solucaoData.map((entry, index) => (
          <Box 
            key={`legend-${index}`} 
            sx={{ 
              display: 'flex', 
              alignItems: 'center', 
              mx: 1.5, 
              mb: 1
            }}
          >
            <Box 
              sx={{ 
                width: 12, 
                height: 12, 
                backgroundColor: COLORS[index % COLORS.length],
                borderRadius: '50%',
                mr: 1
              }} 
            />
            <Typography variant="body2" color="text.secondary">
              {entry.nome}: {entry.valor}%
            </Typography>
          </Box>
        ))}
      </Box>
    );
  };

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
      <AppBar position="static" elevation={0}>
        <Toolbar>
          <IconButton
            size="large"
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2 }}
            onClick={toggleDrawer}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Sistema de Monitoramento de Boas Práticas
          </Typography>
          <Avatar sx={{ bgcolor: theme.palette.secondary.main }}>
            <PersonIcon />
          </Avatar>
        </Toolbar>
      </AppBar>
      
      <Drawer
        anchor="left"
        open={drawerOpen}
        onClose={toggleDrawer}
      >
        {drawerContent}
      </Drawer>

      <Container maxWidth="lg" sx={{ mt: 4, mb: 4, flexGrow: 1 }}>
        <Box sx={{ mb: 4 }}>
          <Typography variant="h4" component="h1" gutterBottom>
            Dashboard de Monitoramento
          </Typography>
          <Typography variant="subtitle1" color="text.secondary">
            Visualize e analise os dados de higienização de vegetais
          </Typography>
        </Box>

        <Stack spacing={3}>
          {/* Cartões de resumo */}
          <Stack direction={{ xs: 'column', sm: 'row' }} spacing={2}>
            <Card sx={{ flex: 1, bgcolor: 'primary.light', color: 'white' }}>
              <CardContent>
                <Typography variant="h5" component="div">
                  85%
                </Typography>
                <Typography variant="body2">
                  Conformidade Geral
                </Typography>
              </CardContent>
            </Card>
            <Card sx={{ flex: 1, bgcolor: 'secondary.light' }}>
              <CardContent>
                <Typography variant="h5" component="div">
                  152
                </Typography>
                <Typography variant="body2">
                  Processos Registrados
                </Typography>
              </CardContent>
            </Card>
            <Card sx={{ flex: 1, bgcolor: 'info.light', color: 'white' }}>
              <CardContent>
                <Typography variant="h5" component="div">
                  12
                </Typography>
                <Typography variant="body2">
                  Vegetais Monitorados
                </Typography>
              </CardContent>
            </Card>
            <Card sx={{ flex: 1, bgcolor: 'success.light', color: 'white' }}>
              <CardContent>
                <Typography variant="h5" component="div">
                  4
                </Typography>
                <Typography variant="body2">
                  Soluções Utilizadas
                </Typography>
              </CardContent>
            </Card>
          </Stack>

          {/* Gráficos principais - Ajustado para 55% / 45% em vez de 2:1 */}
          <Stack direction={{ xs: 'column', md: 'row' }} spacing={2}>
            {/* Gráfico de barras - Conformidade por vegetal - Reduzido */}
            <Card sx={{ flex: 55 }}>
              <CardHeader 
                title="Conformidade por Vegetal" 
                subheader="Percentual de processos dentro, abaixo e acima do padrão"
              />
              <CardContent>
                <Box sx={{ height: 400 }}>
                  <ResponsiveContainer width="100%" height="100%">
                    <BarChart
                      data={conformidadeData}
                      margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
                    >
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="nome" />
                      <YAxis />
                      <Tooltip 
                        formatter={(value) => [`${value}%`, 'Percentual']}
                        contentStyle={{ 
                          backgroundColor: theme.palette.background.paper,
                          borderRadius: 8,
                          boxShadow: theme.shadows[3],
                          border: 'none'
                        }}
                      />
                      <Legend />
                      <Bar 
                        dataKey="dentroPadrao" 
                        name="Dentro do Padrão" 
                        stackId="a" 
                        fill={theme.palette.success.main}
                        animationDuration={1500}
                        animationEasing="ease-in-out"
                      />
                      <Bar 
                        dataKey="abaixoPadrao" 
                        name="Abaixo do Padrão" 
                        stackId="a" 
                        fill={theme.palette.warning.main}
                        animationDuration={1500}
                        animationEasing="ease-in-out"
                      />
                      <Bar 
                        dataKey="acimaPadrao" 
                        name="Acima do Padrão" 
                        stackId="a" 
                        fill={theme.palette.error.main}
                        animationDuration={1500}
                        animationEasing="ease-in-out"
                      />
                    </BarChart>
                  </ResponsiveContainer>
                </Box>
              </CardContent>
            </Card>

            {/* Gráfico de pizza - Soluções utilizadas - Ampliado */}
            <Card sx={{ flex: 45 }}>
              <CardHeader 
                title="Soluções Utilizadas" 
                subheader="Distribuição percentual por tipo"
              />
              <CardContent>
                <Box sx={{ height: 350, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                  <ResponsiveContainer width="100%" height="100%">
                    <PieChart>
                      <Pie
                        data={solucaoData}
                        cx="50%"
                        cy="50%"
                        labelLine={false}
                        outerRadius={isMobile ? 80 : 120}
                        innerRadius={isMobile ? 40 : 60}
                        fill="#8884d8"
                        dataKey="valor"
                        nameKey="nome"
                        label={renderCustomizedLabel}
                        animationDuration={1500}
                        animationEasing="ease-in-out"
                      >
                        {solucaoData.map((_, index) => (
                          <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                        ))}
                      </Pie>
                      <Tooltip 
                        formatter={(value) => [`${value}%`, 'Percentual']}
                        contentStyle={{ 
                          backgroundColor: theme.palette.background.paper,
                          borderRadius: 8,
                          boxShadow: theme.shadows[3],
                          border: 'none'
                        }}
                      />
                    </PieChart>
                  </ResponsiveContainer>
                </Box>
                {/* Legenda personalizada com percentuais em linha abaixo */}
                {renderCustomLegend()}
              </CardContent>
            </Card>
          </Stack>

          {/* Gráficos secundários */}
          <Stack direction={{ xs: 'column', md: 'row' }} spacing={2}>
            {/* Gráfico de linha - Tendência de conformidade */}
            <Card sx={{ flex: 1 }}>
              <CardHeader 
                title="Tendência de Conformidade" 
                subheader="Evolução mensal do percentual de conformidade"
              />
              <CardContent>
                <Box sx={{ height: 300 }}>
                  <ResponsiveContainer width="100%" height="100%">
                    <LineChart
                      data={tendenciaData}
                      margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
                    >
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="mes" />
                      <YAxis domain={[70, 100]} />
                      <Tooltip 
                        formatter={(value) => [`${value}%`, 'Conformidade']}
                        contentStyle={{ 
                          backgroundColor: theme.palette.background.paper,
                          borderRadius: 8,
                          boxShadow: theme.shadows[3],
                          border: 'none'
                        }}
                      />
                      <Legend />
                      <Line 
                        type="monotone" 
                        dataKey="conformidade" 
                        name="Conformidade" 
                        stroke={theme.palette.primary.main} 
                        strokeWidth={3}
                        dot={{ r: 6, fill: theme.palette.primary.main }}
                        activeDot={{ r: 8, fill: theme.palette.primary.dark }}
                        animationDuration={1500}
                        animationEasing="ease-in-out"
                      />
                    </LineChart>
                  </ResponsiveContainer>
                </Box>
              </CardContent>
            </Card>

            {/* Gráfico de área - Evolução de processos */}
            <Card sx={{ flex: 1 }}>
              <CardHeader 
                title="Evolução de Processos" 
                subheader="Quantidade mensal de processos registrados"
              />
              <CardContent>
                <Box sx={{ height: 300 }}>
                  <ResponsiveContainer width="100%" height="100%">
                    <AreaChart
                      data={[
                        { mes: 'Jan', quantidade: 18 },
                        { mes: 'Fev', quantidade: 22 },
                        { mes: 'Mar', quantidade: 25 },
                        { mes: 'Abr', quantidade: 30 },
                        { mes: 'Mai', quantidade: 28 },
                        { mes: 'Jun', quantidade: 32 },
                      ]}
                      margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
                    >
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="mes" />
                      <YAxis />
                      <Tooltip 
                        formatter={(value) => [value, 'Quantidade']}
                        contentStyle={{ 
                          backgroundColor: theme.palette.background.paper,
                          borderRadius: 8,
                          boxShadow: theme.shadows[3],
                          border: 'none'
                        }}
                      />
                      <Legend />
                      <Area 
                        type="monotone" 
                        dataKey="quantidade" 
                       
(Content truncated due to size limit. Use line ranges to read in chunks)