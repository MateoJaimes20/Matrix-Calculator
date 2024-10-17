import customtkinter as ctk

class Documentacion:
    def __init__(self, parent):
        # Crear frame con scrollbar, ahora usando "self.frame"
        self.frame = ctk.CTkScrollableFrame(parent, width=630, height=680)
        self.frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        # Crear título principal
        self.titulo = ctk.CTkLabel(self.frame, text="Calculadora de Matrices y Escalares", font=("Helvetica", 24, "bold"), padx=10, pady=10)
        self.titulo.pack(fill=ctk.BOTH, pady=10)

        # Crear sección de introducción
        self.introduccion_frame = ctk.CTkFrame(self.frame, corner_radius=10)
        self.introduccion_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=5)

        self.introduccion_label = ctk.CTkLabel(
            self.introduccion_frame, 
            text="Este programa te permite realizar operaciones con matrices y escalares de forma rápida y eficiente.",
            font=("Helvetica", 14), justify="left", wraplength=500
        )
        self.introduccion_label.pack(pady=5)

        # Crear sección de instrucciones generales
        self.instrucciones_frame = self.crear_seccion(self.frame, "Instrucciones Generales")

        instrucciones_text = (
            "1. **Seleccionar Modo**: Elige entre \"Multiplicación de Matrices\" o \"Multiplicación por Escalar\".\n\n"
            "2. **Entrada de Datos**:\n"
            "   - **Multiplicación de Matrices**: Ingresa las dimensiones de las matrices.\n"
            "   - **Multiplicación por Escalar**: Ingresa el valor del escalar.\n\n"
            "3. **Calcular**: Haz clic en \"Calcular\" para obtener el resultado.\n"
        )
        self.crear_texto_instrucciones(self.instrucciones_frame, instrucciones_text)

        # Crear sección de funcionalidades adicionales
        self.funcionalidades_frame = self.crear_seccion(self.frame, "Funcionalidades Adicionales")
        
        funcionalidades_text = (
            "- **Determinante**: Calcular el determinante de una matriz cuadrada.\n\n"
            "- **Inversa**: Obtener la matriz inversa si existe.\n\n"
            "- **Transpuesta**: Intercambiar filas por columnas en una matriz.\n\n"
            "- **Rango**: Determinar el rango (número de columnas linealmente independientes).\n"
        )
        self.crear_texto_instrucciones(self.funcionalidades_frame, funcionalidades_text)

        # Crear sección de consejos importantes
        self.consejos_frame = self.crear_seccion(self.frame, "Consejos Importantes")

        consejos_text = (
            "- **Validación de Datos**: Verifica que todos los datos sean correctos antes de calcular.\n\n"
            "- **Errores Comunes**: Asegúrate de que las dimensiones de las matrices sean compatibles para realizar operaciones.\n"
        )
        self.crear_texto_instrucciones(self.consejos_frame, consejos_text)

        # Crear ejemplo de uso
        self.ejemplo_frame = self.crear_seccion(self.frame, "Ejemplo de Uso")

        ejemplo_text = (
            "Para multiplicar dos matrices, selecciona \"Multiplicación de Matrices\", "
            "ingresa las dimensiones, llena las matrices con los valores, y presiona \"Calcular\"."
        )
        self.crear_texto_instrucciones(self.ejemplo_frame, ejemplo_text)

    def crear_seccion(self, parent, titulo):
        """Crea una sección con un título destacado."""
        seccion_frame = ctk.CTkFrame(parent, corner_radius=10)
        seccion_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        seccion_titulo = ctk.CTkLabel(
            seccion_frame, text=titulo, font=("Helvetica", 18, "bold"), padx=10, pady=5
        )
        seccion_titulo.pack(anchor="w", pady=5)

        return seccion_frame

    def crear_texto_instrucciones(self, parent, texto):
        """Crea un texto con estilo para instrucciones o descripciones."""
        instrucciones_label = ctk.CTkLabel(
            parent, text=texto, font=("Helvetica", 13), justify="left", wraplength=500, padx=10
        )
        instrucciones_label.pack(fill=ctk.BOTH, pady=5)

# Crear ventana para probar la clase Documentacion
if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("650x700")
    root.title("Documentación")
    app = Documentacion(root)
    root.mainloop()
