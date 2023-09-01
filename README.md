# Cassette.

Utilidad para pasar guiones escritos en [Fountain](https://fountain.io/) a audio.

Ejemplos de uso:

* Cargamos un fichero de guión en formato [Fountain](https://fountain.io/)
  
```bash
cst="corto"
fountain="corto.fountain"
salida="$(pwd)/corto"
cassette run -j load -p "pname=$cst" -p "fountain=$fountain"
```

* Describimos el guión:
  
```bash
cassette run -j describe -p "pname=$cst"
```

* Obtenemos el timeline y lo completamos que las pistas que enlazan escenas
  
```bash
cassette run -j gettimeline -p "pname=$cst.cst"
```

* Cargamos el timeline al proyecto
  
```bash
cassette run -j loadtimeline -p "pname=$cst" -p "timeline=$cst.cst.yaml"
```

* Renderizamos los dialogos 
  
```bash
cassette run -j renderaudio -p "pname=$cst" -p "storepath=$salida"
```

* Renderizamos las escenas 
  
```bash
cassette run -j renderscene -p "pname=$cst" -p "storepath=$salida"
```

* Renderizamos el guión completo.
  
```bash
cassette run -j renderrecord -p "pname=$cst" -p "storepath=$salida"
```

# Configuración del timeline.

## Voces

```yaml
characters:
  # PEDRO
  - id: 1
    voice:
      tts:
        voiceid: 14
      filter:
        - reverb:
            room_size: 0.1

  # MARIA
  - id: 2
    voice:
      tts:
        voiceid: 29
      filter:
        - reverb:
            room_size: 0.1
```


| Genero | ID | Nombre | Lengua |
|--------|----|--------|--------|
| VoiceGenderFemale |29| Monica |`['es_ES']`| 
| VoiceGenderFemale |31| Paulina |`['es_MX']`| 
| VoiceGenderFemale |37| Tessa |`['en_ZA']`| 
| VoiceGenderMale |14| Jorge |`['es_ES']`| 
| VoiceGenderMale |15| Juan |`['es_MX']`| 
| VoiceGenderMale |8| Diego |`['es_AR']`| 



## Timeline

### Escena

```yaml
  - type: scene
    scene_id: 1
    background: bg
```

### Transición

```yaml 
  - type: sound
    track: sound1
    duration: 8
    volume: inout
```