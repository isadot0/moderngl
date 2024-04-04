import numpy as np
import glm
import pygame as pg
import moderngl as mgl

class BaseModel:
    def __init__(self, app, vao_name, tex_id):
        self.app = app
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self.app.camera

        def get_model_matrix(self):
            m_model = glm.mat4()
            return m_model
        
        def render(self):
            self.update
            self.vao.render()

        def update(self): ...

class Cube(BaseModel):
    def __init__(self, app, vao_name="cube", tex_id=0):
        super().__init__(app, vao_name, tex_id)
        self.on_init()

    def update(self):
        self.texture.use()
        #wrtie in changes for shader
        self.shader_program["m_model"].write(self.m_model)
        self.shader_program['m_view'].write(self.app.camera.m_view)
        self.shader_program["camPos"].write(self.app.camera.position)

    def on_init(self):
        #light
        self.shader_program["light.position"].write(self.app.light.position)
        self.shader_program["light.Ia"].write(self.app.light.Ia)
        self.shader_program["light.Id"].write(self.app.light.Id)
        self.shader_program["light.Is"].write(self.app.light.Is)
        #texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program["u_texture_0"] = 0
        self.texture.use()
        #mvp
        self.shader_program['m_proj'].write(self.app.camera.m_proj)
        self.shader_program['m_view'].write(self.app.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)