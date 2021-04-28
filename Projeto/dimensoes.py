# --------------------- DIMENSOES E DADOS DE CARGA DO CAIXÃO ANALISADO ---------------------


# ---------- Número USP e Delta ----------
A = 62
delta = 0.004 * A + 0.8


#---------- Dimensoes Caixão ----------
C = 600 * delta # [mm]
L = 300 * delta # [mm]
H1 = 150 * delta # [mm]
H2 = 120 * delta # [mm]


#Perfil 1
W_1 = 15 * delta # [mm]
H_1 = 15 * delta # [mm]
t_1 = 1 * delta # [mm]
W1_1 = 5 * delta # [mm]

#Perfil 2
W_2 = 15 * delta # [mm]
H_2 = 10 * delta # [mm]
t1_2 = 1 * delta # [mm]
t2_2 = 1 * delta # [mm]


# ---------- Materiais ----------

# Material 1 - Al 7475-T6 
# Usado para os perfis

E_1 = 7.2 * 10^(10) #[N/m]
nu_1 = 0.32



# Material 2 - Al 2024-T3
# Usado para revestimento, alma da longarina e alma da nervura
revestimento = 1.5 * delta # [mm]
alma_longarina = 1.5 * delta # [mm]
alma_nervura = 1.5 * delta # [mm]

E_2 = 6.9 * 10^(10) #[N/m]
nu_2 = 0.33 



#---------- Dados de Carga ----------
W_bruto = 4003.4 # [N]
nz_max = 0
W_semi_asa = 1000
F_lim = 91000 - (nz_max * W_semi_asa) # [N]

F1 = 0.75 * F_lim # [N]
F2 = 0.25 * F_lim # [N]
F3 = 0.1 * F_lim # [N]
F4 = 0.15 * F_lim # [N]

