# organizador
#### Organiza archivos en carpetas teniendo como referencia las similitudes en sus nombres.

### Instalación:

```pip install organizador```

### Ejemplo:

- Ejecuta `python3 organizador/main.py` dentro del directorio a ordenar.
```
aj@Armando:~/Nueva carpeta$ ls

'100-man no Inochi no Ue ni Ore wa Tatteiru Episodio 11.mp4'  'Bungou Stray Dogs Wan! Episodio 3 Sub Español — AnimeFLV.mp4'
'100-man no Inochi no Ue ni Ore wa Tatteiru Episodio 12.mp4'  'Bungou Stray Dogs Wan! Episodio 3.mp4'
'100-man no Inochi no Ue ni Ore wa Tatteiru Episodio 3.mp4'   'Dr. Stone- Stone Wars Episodio 1 Sub Español — AnimeFLV.mp4'
 227-2.mp4                                                     e822b6f12aa3cb53a66c633526439c71-480p.mp4
 baki-dai-reitaisaihen-10.mp4                                 'Enen no Shouboutai Ni no Shou Episodio 16.mp4'
 baki-dai-reitaisaihen-11.mp4                                 'Spirit Sword Sovereign 4 Episodio 29.mp4'
 baki-dai-reitaisaihen-12.mp4                                 'Spirit Sword Sovereign 4 Episodio 30.mp4'
 baki-dai-reitaisaihen-13.mp4                                 'Spirit Sword Sovereign 4 Episodio 31.mp4'
 baki-dai-reitaisaihen-1.mp4                                  'Spirit Sword Sovereign 4 Episodio 32.mp4'
 baki-dai-reitaisaihen-2.mp4                                  'Spirit Sword Sovereign 4 Episodio 33.mp4'
 baki-dai-reitaisaihen-3.mp4                                  'Spirit Sword Sovereign 4 Episodio 34.mp4'
 baki-dai-reitaisaihen-4.mp4                                  'Spirit Sword Sovereign 4 Episodio 36.mp4'
 baki-dai-reitaisaihen-5.mp4                                  'Spirit Sword Sovereign 4 Episodio 37.mp4'
 baki-dai-reitaisaihen-6.mp4                                  'Spirit Sword Sovereign 4 Episodio 39.mp4'
 baki-dai-reitaisaihen-7.mp4                                  'Spirit Sword Sovereign 4 Episodio 40 Sub Español.mp4'
 baki-dai-reitaisaihen-8.mp4                                  'Spirit Sword Sovereign 4 Episodio 41.mp4'
 baki-dai-reitaisaihen-9.mp4                                  'Spirit Sword Sovereign 4 Episodio 42.mp4'
'Bungou Stray Dogs Wan! Episodio 1.mp4'                       'Spirit Sword Sovereign 4 Episodio 43 Sub Español.mp4'
'Bungou Stray Dogs Wan! Episodio 2.mp4'

aj@Armando:~/Nueva carpeta$ python3 organizador/main.py 

Organizando archivos:

Buscando: |████████████████████████████████████████| 100.0 %   
Reprocesando: |████████████████████████████████████████| 100.0 %   

Caracteres similares: 4
Reprocesando resultados: 4

Terminado en 0.05 segundos.

aj@Armando:~/Nueva carpeta$ tree
.
├── 227-2.mp4
├── Dr. Stone- Stone Wars Episodio 1 Sub Español — AnimeFLV.mp4
├── e822b6f12aa3cb53a66c633526439c71-480p.mp4
├── Enen no Shouboutai Ni no Shou Episodio 16.mp4
└── Organizados
    ├── 100-man no Inochi no Ue ni Ore wa Tatteiru Episodio
    │   ├── 100-man no Inochi no Ue ni Ore wa Tatteiru Episodio 11.mp4
    │   ├── 100-man no Inochi no Ue ni Ore wa Tatteiru Episodio 12.mp4
    │   └── 100-man no Inochi no Ue ni Ore wa Tatteiru Episodio 3.mp4
    ├── baki-dai-reitaisaihen-
    │   ├── baki-dai-reitaisaihen-10.mp4
    │   ├── baki-dai-reitaisaihen-11.mp4
    │   ├── baki-dai-reitaisaihen-12.mp4
    │   ├── baki-dai-reitaisaihen-13.mp4
    │   ├── baki-dai-reitaisaihen-1.mp4
    │   ├── baki-dai-reitaisaihen-2.mp4
    │   ├── baki-dai-reitaisaihen-3.mp4
    │   ├── baki-dai-reitaisaihen-4.mp4
    │   ├── baki-dai-reitaisaihen-5.mp4
    │   ├── baki-dai-reitaisaihen-6.mp4
    │   ├── baki-dai-reitaisaihen-7.mp4
    │   ├── baki-dai-reitaisaihen-8.mp4
    │   └── baki-dai-reitaisaihen-9.mp4
    ├── Bungou Stray Dogs Wan! Episodio
    │   ├── Bungou Stray Dogs Wan! Episodio 1.mp4
    │   ├── Bungou Stray Dogs Wan! Episodio 2.mp4
    │   ├── Bungou Stray Dogs Wan! Episodio 3 Sub Español — AnimeFLV.mp4
    │   └── Bungou Stray Dogs Wan! Episodio 3.mp4
    └── Spirit Sword Sovereign 4 Episodio
        ├── Spirit Sword Sovereign 4 Episodio 29.mp4
        ├── Spirit Sword Sovereign 4 Episodio 30.mp4
        ├── Spirit Sword Sovereign 4 Episodio 31.mp4
        ├── Spirit Sword Sovereign 4 Episodio 32.mp4
        ├── Spirit Sword Sovereign 4 Episodio 33.mp4
        ├── Spirit Sword Sovereign 4 Episodio 34.mp4
        ├── Spirit Sword Sovereign 4 Episodio 36.mp4
        ├── Spirit Sword Sovereign 4 Episodio 37.mp4
        ├── Spirit Sword Sovereign 4 Episodio 39.mp4
        ├── Spirit Sword Sovereign 4 Episodio 40 Sub Español.mp4
        ├── Spirit Sword Sovereign 4 Episodio 41.mp4
        ├── Spirit Sword Sovereign 4 Episodio 42.mp4
        └── Spirit Sword Sovereign 4 Episodio 43 Sub Español.mp4

5 directories, 37 files
```
