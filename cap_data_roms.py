# Script para a captação de dados, a ser implementado no container docker, seguindo os seguintes passos:
# 1. Gera um dataset do NetCDF geral com as variáveis de interesse 
# 2. Salva em no diretório vinculado ao volume do host

import xarray as xr
from datetime import datetime
import os

#COM DATAS ESECIFICAR PARA TESTE
# Importando o nc do roms
dir_out_roms = f"home/william/COAWST/ROMS_OUTPUTS/2025092400"
file_out_roms = f"{dir_out_roms}/procosta_his_20250924.nc"

# Diretório de saída customizado
dir_save = f"/home/CIEX/out_ROMS_CIEX_20250924"
os.makedirs(dir_save, exist_ok=True)
file_save = f"{dir_save}/roms_dataset_20250924.nc"

'''# Criando dataset da saída do ROMS
# Importando o nc do roms
dir_out_roms = f"home/william/COAWST/ROMS_OUTPUTS/{datetime.now().strftime('%Y%m%d')}00"
file_out_roms = f"{dir_out_roms}/procosta_his_{datetime.now().strftime('%Y%m%d')}.nc"

# Diretório de saída customizado
dir_save = f"/home/CIEX/out_ROMS_CIEX_{datetime.now().strftime('%Y%m%d')}"
os.makedirs(dir_save, exist_ok=True)
file_save = f"{dir_save}/roms_dataset_{datetime.now().strftime('%Y%m%d')}.nc"'''

ds = xr.open_dataset(file_out_roms)

try:
    var = [
    # Variáveis principais
    'temp',      # Temperatura da água (°C)
    'salt',      # Salinidade (psu)
    'u',         # Componente zonal (leste-oeste) da corrente (m/s)
    'v',         # Componente meridional (norte-sul) da corrente (m/s)
    'Uwind',     # Vento zonal na superfície (m/s)
    'Vwind',     # Vento meridional na superfície (m/s)

    # Coordenadas temporais e verticais
    'ocean_time', # Tempo da simulação (segundos desde a data inicial, convertido em datetime pelo xarray)
    's_rho',      # Coordenada vertical sigma (níveis normalizados, -1 até 0)

    # Coordenadas horizontais da grade (longitude/latitude)
    'lon_rho', 'lat_rho',   # Longitude/latitude nos pontos "rho" 
    'lon_u', 'lat_u',       # Longitude/latitude nos pontos "u"
    'lon_v', 'lat_v',       # Longitude/latitude nos pontos "v"

    # Informações da grade
    'h',          # Batimetria (profundidade do fundo em metros, positiva)
    'mask_rho',   # Máscara nos pontos "rho" (1 = mar, 0 = terra)
    'mask_u',     # Máscara nos pontos "u"
    'mask_v'      # Máscara nos pontos "v"
]

    # Cria novo dataset com as var de interesse 
    ds_out_roms = ds[var]
    
    # Salva no diretório
    ds_out_roms.to_netcdf(file_save)
    print("✅dataset roms gerado com sucesso")
except:
    print("❌Falha ao gerar dataset roms")

