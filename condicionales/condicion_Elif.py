    ' Verificar si hay alguna selección activa
    If Not Application.ActiveCell Is Nothing Then
        Dim respuesta As VbMsgBoxResult
        respuesta = MsgBox("¿Está seguro de que desea abandonar la operación actual?", vbYesNo + vbQuestion, "Confirmar")
        
        If respuesta = vbNo Then
            Exit Sub ' Si el usuario selecciona No, salir de la macro
        End If
    End If