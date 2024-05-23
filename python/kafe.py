import csv
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit
from scipy.integrate import odeint

import numpy as np

# Inicializace proměnných
temperatures = []
times = []

# Načtení souboru
t = 0
with open(r"kafe.txt") as file:
    csvReader = csv.reader(file, delimiter='\t')

    for row in csvReader:

        if len(row) < 3:
            continue

        temperatures.append(float(row[1]))
        times.append(t)
        t += 10

plt.plot(times, temperatures, 'o', label="Naměřená data")
plt.xlabel(r"$t\ [s]$")
plt.ylabel(r"$T\ [\degree C]$")
plt.show()

# Převedeme seznamy na řady
temperatures = np.array(temperatures)
times = np.array(times)

T0 = temperatures[0]    # Počáteční teplota
T_out = 20              # Teplota okolí

""" Newtonův zákon chladnutí """
def model_exp(t, alpha):
    return (T0 - T_out) * np.exp(-alpha * t) + T_out

fit, cm = curve_fit(model_exp, times, temperatures, p0=1e-4)
alpha_fit = fit[0]
sigma_alpha = np.sqrt(cm[0, 0])

temperatures_exp = model_exp(times, alpha_fit)
residua_exp = np.sqrt(sum((temperatures - temperatures_exp)**2))

print(f"Newton: alpha = {alpha_fit} +- {sigma_alpha}, R = {residua_exp}")

plt.scatter(times, temperatures, label="Naměřená data")
plt.plot(times, temperatures_exp, "red", label=f"Newtonův zákon chladnutí")
plt.xlabel(r"t [s]")
plt.ylabel(r"T [$\degree$C]")
plt.legend()
plt.show()

""" Newtonův zákon chladnutí s fitovanou teplotou okolí """
def model_out(t, alpha, T_out):
    return (T0 - T_out) * np.exp(-alpha * t) + T_out

# Fitování zadané křivky
fit, cm = curve_fit(model_out, times, temperatures, p0=(1e-4, 20))
alpha_out_fit, T_out_fit = fit
sigma_alpha_out = np.sqrt(cm[0, 0])
sigma_T_out = np.sqrt(cm[1, 1])

temperatures_out = model_out(times, alpha_out_fit, T_out_fit)
residua_out = np.sqrt(sum((temperatures - temperatures_out)**2))

print(f"Newton: alpha = {alpha_out_fit} +- {sigma_alpha_out}, T_out = {T_out_fit} +- {sigma_T_out}, R = {residua_out}")

plt.scatter(times, temperatures, label="Naměřená data")
plt.plot(times, temperatures_out, "red", label=r"Newtonův zákon chladnutí s $T_{\mathrm{out}}$")
plt.xlabel(r"t [s]")
plt.ylabel(r"T [$\degree$C]")
plt.legend()
plt.show()

T_abs = 273.15

""" Newton + dodatečný člen simulující vyzařování """
def model_rad_ode(temperature, time, alpha, beta):
    """ Diferenciální rovnice chladnutí (Newtonův zákon chladnutí + dodatečný člen se čtvrtou mocninou - záření) """
    return -alpha * (temperature - T_out) - beta * ((temperature + T_abs)**4 - (T_out + T_abs)**4)

def model_rad_solution(times, alpha, beta):
    """ Řešení diferenciální rovnice """
    temperatures = odeint(model_rad_ode, T0, times, args=(alpha, beta))
    return temperatures[:,0]    # Jen teploty

fit, cm = curve_fit(model_rad_solution, times, temperatures, p0=(1e-3, 1e-10))
alpha_rad_fit, beta_rad_fit = fit

sigma_alpha_rad = np.sqrt(cm[0, 0])
sigma_beta_rad = np.sqrt(cm[1, 1])

temperatures_rad = model_rad_solution(times, alpha_rad_fit, beta_rad_fit)
residua_rad = np.sqrt(sum((temperatures - temperatures_rad)**2))

print(f"alpha = {alpha_rad_fit} +- {sigma_alpha_rad}, beta= {beta_rad_fit} +- {sigma_beta_rad}, R = {residua_rad}")

plt.scatter(times, temperatures, label="Naměřená data")
plt.plot(times, temperatures_rad, "red", label="Newton + vyzařování")
plt.xlabel(r"t [s]")
plt.ylabel(r"T [$\degree$C]")
plt.legend()
plt.show()

""" Newton + umělý člen daný druhým členem Taylorova rozvoje (T - T_out) """
def model_2_ode(temperature, time, alpha, beta):
    """ Diferenciální rovnice chladnutí (Newtonův zákon chladnutí + dodatečný člen) """
    return -alpha * (temperature - T_out) - beta * ((temperature - T_out)**2)

def model_2_solution(times, alpha, beta):
    """ Řešení diferenciální rovnice """
    temperatures = odeint(model_2_ode, T0, times, args=(alpha, beta))
    return temperatures[:,0]    # Jen teploty

fit, cm = curve_fit(model_2_solution, times, temperatures, p0=(1e-3, 1e-6))
alpha_2_fit, beta_2_fit = fit

sigma_alpha_2 = np.sqrt(cm[0, 0])
sigma_beta_2 = np.sqrt(cm[1, 1])

temperatures_2 = model_2_solution(times, alpha_2_fit, beta_2_fit)
residua_2 = np.sqrt(sum((temperatures - temperatures_2)**2))

print(f"alpha = {alpha_2_fit} +- {sigma_alpha_2}, beta= {beta_2_fit} +- {sigma_beta_2}, R = {residua_2}")

plt.scatter(times, temperatures, label="Naměřená data")
plt.plot(times, temperatures_2, "red", label="Newton + druhý člen Taylorova rozvoje")
plt.xlabel(r"t [s]")
plt.ylabel(r"T [$\degree$C]")
plt.legend()
plt.show()


""" Uložení výsledků """
# newline="" je nutný parametr ve windows; jinak program vkládá mezi data prázdné řádky
with open(r"kafe_model.txt", "w", newline="") as file:
    csvWriter = csv.writer(file, delimiter='\t')
    csvWriter.writerow(["t [s]", "Texp [C]", "Texpout [C]", "Trad [C]", "Ttaylor [C]"])

 #   for row in zip(times, temperatures, temperatures_exp, temperatures_out, temperatures_rad, temperatures_2):
 #       csvWriter.writerow(row)
        
    csvWriter.writerows(zip(times, temperatures, temperatures_exp, temperatures_out, temperatures_rad, temperatures_2))
