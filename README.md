# organizador
#### Organiza archivos en carpetas teniendo como referencia las similitudes en sus nombres.

### Instalación:

```pip install organizador```

### Ejemplo:

- Ejecuta `python3 organizador/main.py` dentro del directorio a ordenar.
```
aj@Armando:~/Nueva carpeta$ tree   
.
├── Borrar
│   └── Mahoutsukai Reimeiki Episodio
├── Organizados
│   └── Dr. Stone- Stone Wars Episodio
├── Nuevos
├── Errores
├── Dr. Stone- Stone Wars Episodio 1 Sub Español — AnimeFLV.mp4
├── Dr. Stone- Stone Wars Episodio 10 Sub Español — AnimeFLV.mp4
├── Dr. Stone- Stone Wars Episodio 11.mp4
├── Dr. Stone- Stone Wars Episodio 2 Sub Español — AnimeFLV.mp4
├── Dr. Stone- Stone Wars Episodio 3 Sub Español — AnimeFLV.mp4
├── Dr. Stone- Stone Wars Episodio 4.mp4
├── Dr. Stone- Stone Wars Episodio 5.mp4
├── Dr. Stone- Stone Wars Episodio 6.mp4
├── Dr. Stone- Stone Wars Episodio 7 Sub Español — AnimeFLV.mp4
├── Dr. Stone- Stone Wars Episodio 8 Sub Español — AnimeFLV.mp4
├── Dr. Stone- Stone Wars Episodio 9 Sub Español — AnimeFLV.mp4
├── Mahoutsukai Reimeiki Episodio 10.mp4
├── Mahoutsukai Reimeiki Episodio 1.mp4
├── Mahoutsukai Reimeiki Episodio 2.mp4
├── Mahoutsukai Reimeiki Episodio 3.mp4
├── Mahoutsukai Reimeiki Episodio 5.mp4
├── Mahoutsukai Reimeiki Episodio 6.mp4
├── Mahoutsukai Reimeiki Episodio 8.mp4
├── Spy x Family Episodio 10.mp4
├── Spy x Family Episodio 11.mp4
├── Spy x Family Episodio 12.mp4
├── Spy x Family Episodio 1.mp4
├── Spy x Family Episodio 2.mp4
├── Spy x Family Episodio 3.mp4
├── Spy x Family Episodio 4.mp4
├── Spy x Family Episodio 5.mp4
├── Spy x Family Episodio 6.mp4
├── Spy x Family Episodio 7.mp4
├── Spy x Family Episodio 8.mp4
├── Spy x Family Episodio 9.mp4
├── Summertime Render Episodio 4.mp4
├── Summertime Render Episodio 7.mp4
└── Summertime Render Episodio 8.mp4

6 directories, 33 files

aj@Armando:~/Nueva carpeta$ python3 organizador/main.py

Organizando archivos:


Buscando al 85%: |████████████████████████████████████████| 100.0 %   
Similares: 2

Reprocesando al 90%: |████████████████████████████████████████| 100.0 %   
Similares: 2

arch iniciales: 33
arch organizados: 11
arch borrar: 7
arch nuevos: 15
arch sin procesar: 0

Terminado en 6.06 segundos.

aj@Armando:~/Nueva carpeta$ tree
.
├── Borrar
│   └── Mahoutsukai Reimeiki Episodio
│       ├── Mahoutsukai Reimeiki Episodio 10.mp4
│       ├── Mahoutsukai Reimeiki Episodio 1.mp4
│       ├── Mahoutsukai Reimeiki Episodio 2.mp4
│       ├── Mahoutsukai Reimeiki Episodio 3.mp4
│       ├── Mahoutsukai Reimeiki Episodio 5.mp4
│       ├── Mahoutsukai Reimeiki Episodio 6.mp4
│       └── Mahoutsukai Reimeiki Episodio 8.mp4
├── Errores
│   ├── errores_Borrar.txt
│   ├── errores_Organizados.txt
│   └── errores_similares.txt
├── Nuevos
│   ├── Spy x Family Episodio
│   │   ├── Spy x Family Episodio 10.mp4
│   │   ├── Spy x Family Episodio 11.mp4
│   │   ├── Spy x Family Episodio 12.mp4
│   │   ├── Spy x Family Episodio 1.mp4
│   │   ├── Spy x Family Episodio 2.mp4
│   │   ├── Spy x Family Episodio 3.mp4
│   │   ├── Spy x Family Episodio 4.mp4
│   │   ├── Spy x Family Episodio 5.mp4
│   │   ├── Spy x Family Episodio 6.mp4
│   │   ├── Spy x Family Episodio 7.mp4
│   │   ├── Spy x Family Episodio 8.mp4
│   │   └── Spy x Family Episodio 9.mp4
│   └── Summertime Render Episodio
│       ├── Summertime Render Episodio 4.mp4
│       ├── Summertime Render Episodio 7.mp4
│       └── Summertime Render Episodio 8.mp4
└── Organizados
    └── Dr. Stone- Stone Wars Episodio
        ├── Dr. Stone- Stone Wars Episodio 1 Sub Español — AnimeFLV.mp4
        ├── Dr. Stone- Stone Wars Episodio 10 Sub Español — AnimeFLV.mp4
        ├── Dr. Stone- Stone Wars Episodio 11.mp4
        ├── Dr. Stone- Stone Wars Episodio 2 Sub Español — AnimeFLV.mp4
        ├── Dr. Stone- Stone Wars Episodio 3 Sub Español — AnimeFLV.mp4
        ├── Dr. Stone- Stone Wars Episodio 4.mp4
        ├── Dr. Stone- Stone Wars Episodio 5.mp4
        ├── Dr. Stone- Stone Wars Episodio 6.mp4
        ├── Dr. Stone- Stone Wars Episodio 7 Sub Español — AnimeFLV.mp4
        ├── Dr. Stone- Stone Wars Episodio 8 Sub Español — AnimeFLV.mp4
        └── Dr. Stone- Stone Wars Episodio 9 Sub Español — AnimeFLV.mp4

8 directories, 36 files

```
