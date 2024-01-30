from manim import *

# Define parameters
num_dots = 8
radius = 2
amplitude = 0.25  # Amplitude of sinusoidal motion
frequency = 4  # Frequency of sinusoidal motion
duration = 4*np.pi

config.background_color = "#000000"

# Calculate initial positions of dots
initial_positions = [
    radius * np.array([
        np.cos(2 * np.pi * i / num_dots),
        np.sin(2 * np.pi * i / num_dots),
        0
    ])
    for i in range(num_dots)
]

alpha = ValueTracker()


class PlusPolarization(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        dots = always_redraw(
            lambda: VGroup(
                *[
                    Dot([
                            initial_positions[i][0] + amplitude * np.sin(frequency * alpha.get_value()) * initial_positions[i][0],
                            initial_positions[i][1] - amplitude * np.sin(frequency * alpha.get_value()) * initial_positions[i][1],
                            0
                        ],
                        color=BLACK
                    )
                    for i in range(num_dots)
                ])
        )
        self.add(dots, Dot(ORIGIN, color=BLACK))
        self.play(alpha.animate.set_value(duration), rate_func=linear, run_time=duration)
        


class CrossPolarization(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        dots = always_redraw(
            lambda: VGroup(
                *[
                    Dot([
                            initial_positions[i][0] + amplitude * np.sin(frequency * alpha.get_value()) * initial_positions[i][1],
                            initial_positions[i][1] + amplitude * np.sin(frequency * alpha.get_value()) * initial_positions[i][0],
                            0
                        ],
                        color=BLACK
                    )
                    for i in range(num_dots)
                ])
        )
        self.add(dots, Dot(ORIGIN, color=BLACK))
        self.play(alpha.animate.set_value(duration), rate_func=linear, run_time=duration)



class CircularRightPolarization(Scene):
        def construct(self):
            self.camera.background_color = WHITE
            dots = always_redraw(
                lambda: VGroup(
                    *[
                        Dot([
                                initial_positions[i][0] + amplitude / np.sqrt(2) * (np.sin(frequency * alpha.get_value()) * initial_positions[i][0] + np.sin(frequency * alpha.get_value() + np.pi/2) * initial_positions[i][1]),
                                initial_positions[i][1] + amplitude / np.sqrt(2) * (-np.sin(frequency * alpha.get_value()) * initial_positions[i][1] + np.sin(frequency * alpha.get_value() + np.pi/2) * initial_positions[i][0]),
                                0
                            ],
                            color=BLACK
                        )
                        for i in range(num_dots)
                    ])
            )
            self.add(dots, Dot(ORIGIN, color=BLACK))
            self.play(alpha.animate.set_value(duration), rate_func=linear, run_time=duration)



class CircularLeftPolarization(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        dots = always_redraw(
            lambda: VGroup(
                *[
                    Dot([
                                initial_positions[i][0] + amplitude / np.sqrt(2) * (np.sin(frequency * alpha.get_value()) * initial_positions[i][0] - np.sin(frequency * alpha.get_value() + np.pi/2) * initial_positions[i][1]),
                                initial_positions[i][1] + amplitude / np.sqrt(2) * (-np.sin(frequency * alpha.get_value()) * initial_positions[i][1] - np.sin(frequency * alpha.get_value() + np.pi/2) * initial_positions[i][0]),
                                0
                            ],
                            color=BLACK
                        )
                    for i in range(num_dots)
                ])
        )
        self.add(dots, Dot(ORIGIN, color=BLACK))
        self.play(alpha.animate.set_value(duration), rate_func=linear, run_time=duration)