Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='ImageMixin',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='image.mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Image Mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='image_1920', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Image', kind=None)],
                        keywords=[
                            keyword(
                                arg='max_width',
                                value=Constant(value=1920, kind=None),
                            ),
                            keyword(
                                arg='max_height',
                                value=Constant(value=1920, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='image_1024', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Image 1024', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='image_1920', kind=None),
                            ),
                            keyword(
                                arg='max_width',
                                value=Constant(value=1024, kind=None),
                            ),
                            keyword(
                                arg='max_height',
                                value=Constant(value=1024, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='image_512', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Image 512', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='image_1920', kind=None),
                            ),
                            keyword(
                                arg='max_width',
                                value=Constant(value=512, kind=None),
                            ),
                            keyword(
                                arg='max_height',
                                value=Constant(value=512, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='image_256', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Image 256', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='image_1920', kind=None),
                            ),
                            keyword(
                                arg='max_width',
                                value=Constant(value=256, kind=None),
                            ),
                            keyword(
                                arg='max_height',
                                value=Constant(value=256, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='image_128', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Image 128', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='image_1920', kind=None),
                            ),
                            keyword(
                                arg='max_width',
                                value=Constant(value=128, kind=None),
                            ),
                            keyword(
                                arg='max_height',
                                value=Constant(value=128, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
