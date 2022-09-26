from sqlalchemy import select

from db_init import Section, Product, session


def get_sections():
    """Получает все имена разделов."""
    sections = session.execute(select(Section))
    section_names = []
    for section in sections.scalars().all():
        section_names.append(section.name)
    return section_names


def get_products():
    """Получает все имена товаров."""
    products = session.execute(select(Product))
    products_names = []
    for product in products.scalars().all():
        products_names.append(product.name)
    return products_names


def get_products_by_section_name(section_name):
    """Получает товары отдельного раздела."""
    section = session.scalars(
        select(Section).where(Section.name == section_name)
    ).first()
    if section:
        products = session.execute(
            select(Product).where(Product.section_id == section.id)
        )
        return products.scalars().all()


def get_product_by_name(product_name):
    """Получает товар по имени."""
    product = session.execute(
        select(Product).where(Product.name == product_name)
    )
    return product.scalars().first()
