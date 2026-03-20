from models import Place

def test_add_place(db_session):
    new_place = Place(name="Эрмитаж", description="Главный музей")
    db_session.add(new_place)
    db_session.commit()

    result = db_session.query(Place).filter_by(name="Эрмитаж").first()
    assert result is not None
    assert result.description == "Главный музей"

def test_update_place(db_session):
    place = Place(name="Парк Горького", description="Старое описание")
    db_session.add(place)
    db_session.commit()

    place.description = "Новое описание"
    db_session.commit()

    updated = db_session.query(Place).filter_by(id=place.id).first()
    assert updated.description == "Новое описание"

def test_delete_place(db_session):
    place = Place(name="Временное место", description="Удалить")
    db_session.add(place)
    db_session.commit()
    place_id = place.id

    db_session.delete(place)
    db_session.commit()

    deleted = db_session.query(Place).filter_by(id=place_id).first()
    assert deleted is None