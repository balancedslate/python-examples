# This is a basic 3D game where the player controls a spaceship
#  and needs to avoid incoming asteroids in Panda3d for Python

# First, we'll import the necessary modules from Panda3D
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from panda3d.core import TextNode
from panda3d.core import LVector3, LVector4
from direct.task.Task import Task
from direct.interval.IntervalGlobal import Sequence
from direct.gui.OnscreenText import OnscreenText
import random

# Next, we'll set up the game class
class Game(ShowBase):
    def __init__(self):
        # Initialize the ShowBase class
        ShowBase.__init__(self)

        # Set up the player's spaceship
        self.spaceship = Actor("models/spaceship", {"move": "models/spaceship-move"})
        self.spaceship.reparentTo(render)
        self.spaceship.loop("move")
        self.spaceship.setPos(0, 0, 0)

        # Set up the incoming asteroids
        self.asteroids = []
        self.addAsteroid()

        # Set up the camera
        self.disableMouse()
        self.camera.setPos(0, -30, 10)
        self.camera.lookAt(0, 0, 0)

        # Set up the lighting
        ambient_light = AmbientLight("ambient_light")
        ambient_light.setColor(LVector4(0.2, 0.2, 0.2, 1))
        directional_light = DirectionalLight("directional_light")
        directional_light.setDirection(LVector3(0, 0, -1))
        directional_light.setColor(LVector4(1, 1, 1, 1))
        render.setLight(render.attachNewNode(ambient_light))
        render.setLight(render.attachNewNode(directional_light))

        # Set up the collision detection
        self.cTrav = CollisionTraverser()
        self.pusher = CollisionHandlerQueue()
        self.collision_sphere = self.spaceship.attachNewNode(CollisionNode("collision_sphere"))
        self.collision_sphere.node().addSolid(CollisionSphere(0, 0, 0, 1))
        self.collision_ray = CollisionRay()
        self.collision_ray_node = CollisionNode("collision_ray")
        self.collision_ray_node.addSolid(self.collision_ray)
        self.collision_ray_node.setFromCollideMask(CollisionNode.getDefaultCollideMask())
        self.collision_ray_node.setIntoCollideMask(CollisionNode.getDefaultIntoCollideMask())
        self.collision_ray_np = camera.attachNewNode(self.collision_ray_np)
                # Set up the game loop
        self.taskMgr.add(self.update, "update")

        # Set up the on-screen instructions
        self.title = OnscreenText(text="Panda3D Asteroid Avoidance Game",
                                  style=1, fg=(1, 1, 1, 1),
                                  pos=(0.9, -0.95), scale=.07)
        self.instructions = OnscreenText(text="Use the arrow keys to move the spaceship. "
                                              "Avoid the incoming asteroids.",
                                        style=1, fg=(1, 1, 1, 1),
                                        pos=(0.9, -0.85), align=TextNode.ALeft, scale=.05)

    def addAsteroid(self):
        # Add a new asteroid at a random x, y position
        asteroid = actor("models/asteroid", {"rotate": "models/asteroid-rotate"})
        asteroid.reparentTo(render)
        asteroid.loop("rotate")
        asteroid.setPos(random.uniform(-10, 10), random.uniform(-10, 10), 10)
        self.asteroids.append(asteroid)

        # Set up the collision detection for the asteroid
        asteroid_collision_sphere = asteroid.attachNewNode(CollisionNode("collision_sphere"))
        asteroid_collision_sphere.node().addSolid(CollisionSphere(0, 0, 0, 1))

        # Set up the movement of the asteroid
        fall_interval = asteroid.posInterval(3, (asteroid.getX(), asteroid.getY(), -10))
        rotate_interval = asteroid.hprInterval(1, (360, 0, 0))
        self.asteroid_movement = Sequence(rotate_interval, fall_interval)
        self.asteroid_movement.loop()

    def update(self, task):
        # Update the positions of the asteroids
        for asteroid in self.asteroids:
            asteroid.setZ(asteroid.getZ() - 0.1)

            # Check if the asteroid has gone off the screen and remove it
            if asteroid.getZ() < -10:
                asteroid.removeNode()
                self.asteroids.remove(asteroid)
                self.addAsteroid()

        # Update the collision detection
        self.cTrav.traverse(render)
        if self.pusher.getNumEntries() > 0:
            self.pusher.sortEntries()
            self.collision_sphere.reparentTo(render)
            self.gameOver()
            return Task.done

        # Check for player input and move the spaceship accordingly
        self.accept("arrow_left", self.spaceship.setX, [self.spaceship.getX() - 0.1])
        self.accept("arrow_right", self.spaceship.setX, [self.spaceship.getX() + 0.1])
        self.accept("arrow_up", self.spaceship.setY, [self.spaceship.getY() + 0.1])
        self.accept("arrow_down", self.spaceship.setY, [self.spaceship.getY() - 0.1])

        # Set up the collision ray to check for collisions with asteroids
                # Set up the collision ray to check for collisions with asteroids
        self.collision_ray.setOrigin(self.camera.getPos())
        self.collision_ray.setDirection(self.camera.getMat().getRow3(1))
        self.cTrav.addCollider(self.collision_ray_np, self.pusher)

        return Task.cont

    def gameOver(self):
        # Stop the game loop and display the game over screen
        self.taskMgr.remove("update")
        self.title.destroy()
        self.instructions.destroy()
        self.gameOverText = OnscreenText(text="Game Over!",
                                        style=1, fg=(1, 1, 1, 1),
                                        pos=(0.9, 0), scale=.1)

# Run the game
game = Game()
game.run()



