

from lib_sprites import ShipSprite, BeeSprite, ShrimpSprite, ShipExplosion
import pygame

from .conftest import get_screen
FILL = (5, 5, 5)



def test_main():
    # galaga_spritesheet = GalagaSpritesheet()
    # galaga_spritesheet2 = GalagaSpritesheet()

    screen = get_screen()

    clock = pygame.time.Clock()

    player_sprites =  pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    non_collision_sprites = pygame.sprite.Group()

    player1 = ShipSprite()
    player_sprites.add(player1)

    player2 = ShipSprite()

    player2.rect.x = 18
    player2.rect.y = 32
    player2.velocity.x = 0
    player2.velocity.y = -1
    player_sprites.add(player2)

    bee = BeeSprite()
    bee.rect.x = 18

    shrimp = ShrimpSprite()
    shrimp.rect.x = 18 * 2

    ship_explosion = ShipExplosion()
    ship_explosion.rect.y = 18

    enemy_sprites.add(bee)
    enemy_sprites.add(shrimp)

    non_collision_sprites.add(ship_explosion)

    # pygame.sprite.spritecollide()¶



    i = 0
    while i < (60 * 10):
        pygame.event.get()
        screen.fill(FILL)

        enemy_sprites.update()
        enemy_sprites.draw(screen)

        non_collision_sprites.update()
        non_collision_sprites.draw(screen)

        player_sprites.update()
        player_sprites.draw(screen)

        for player_sprite in player_sprites:
            blocks_hit_list = pygame.sprite.spritecollide(player_sprite, enemy_sprites, dokill=True)

            if blocks_hit_list:
                ps: pygame.sprite.Sprite = player_sprite
                ps.kill()  # TODO replace with explosion
               
                for block in blocks_hit_list:
                    # tests\test_display_galaga.py <BeeSprite Sprite(in 0 groups)>
                    print(block)




        pygame.display.flip()
        clock.tick(60)
        i += 1
    pass