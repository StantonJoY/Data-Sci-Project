Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='NotePad',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='note.note', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='pad.common', kind=None),
                            Constant(value='note.note', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_pad_fields', ctx=Store())],
                    value=List(
                        elts=[Constant(value='note_pad', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='note_pad_url', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Pad Url', kind=None)],
                        keywords=[
                            keyword(
                                arg='pad_content_field',
                                value=Constant(value='memo', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
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
