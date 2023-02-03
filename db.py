import matplotlib.pyplot as plt
import numpy as np
import wave
import struct

def plot_signal(filename):
    # Abrir el archivo de audio
    wav = wave.open(filename, "r")
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
    frames = wav.readframes(nframes)

    # Convertir los datos a una lista de números
    samples = struct.unpack_from("%dh" % nframes * nchannels, frames)

    # Calcular la amplitud en dB
    samples = np.array(samples) / 2**15
    samples_dB = 20 * np.log10(np.abs(samples))

    # Graficar la señal
    plt.plot(samples_dB)
    plt.show()

def get_mean_dB(filename):
    # Abrir el archivo de audio
    wav = wave.open(filename, "r")
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
    frames = wav.readframes(nframes)

    # Convertir los datos a una lista de números
    samples = struct.unpack_from("%dh" % nframes * nchannels, frames)

    # Calcular la amplitud en dB
    samples = np.array(samples) / 2**15
    samples_dB = 20 * np.log10(np.abs(samples))

    # Calcular la amplitud media en dB
    mean_dB = np.mean(samples_dB)
    
    return mean_dB

def main():
    # Introducir la ruta del archivo de audio
    # Recordar "~/algo.wav" - Fallará si no es un archivo de audio
    # Falta implementar una gestion de errores
    filename = input("Introduce la ruta del archivo de audio: ")

    while True:
        # Mostrar el menú
        # Se añadirán en futuro opciones para:
        # - Guardar el gráfico como imagen en una ruta determinada, asignándole un nombre determinado al fichero en formato png
        print("1. Ver gráfico de la amplitud en dB")
        print("2. Ver la amplitud media en dB")
        print("3. Salir")
        opcion = input("Elije una opción: ")

        try:
            opcion = int(opcion)
        except ValueError:
            print("Opción inválida. Por favor, introduce un número.")
            continue

        if opcion == 1:
            plot_signal(filename)
        elif opcion == 2:
            mean_dB = get_mean_dB(filename)
            print("La amplitud media en dB es:", mean_dB)
        elif opcion == 3:
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Por favor, introduce un número entre 1 y 3.")

if __name__ == "__main__":
    main()
