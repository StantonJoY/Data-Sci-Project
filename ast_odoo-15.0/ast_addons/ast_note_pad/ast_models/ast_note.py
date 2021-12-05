Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=31,
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            lineno=7,
            col_offset=0,
            end_lineno=14,
            end_col_offset=79,
            name='NotePad',
            bases=[
                Attribute(
                    lineno=7,
                    col_offset=14,
                    end_lineno=7,
                    end_col_offset=26,
                    value=Name(lineno=7, col_offset=14, end_lineno=7, end_col_offset=20, id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    lineno=9,
                    col_offset=4,
                    end_lineno=9,
                    end_col_offset=23,
                    targets=[Name(lineno=9, col_offset=4, end_lineno=9, end_col_offset=9, id='_name', ctx=Store())],
                    value=Constant(lineno=9, col_offset=12, end_lineno=9, end_col_offset=23, value='note.note', kind=None),
                    type_comment=None,
                ),
                Assign(
                    lineno=10,
                    col_offset=4,
                    end_lineno=10,
                    end_col_offset=42,
                    targets=[Name(lineno=10, col_offset=4, end_lineno=10, end_col_offset=12, id='_inherit', ctx=Store())],
                    value=List(
                        lineno=10,
                        col_offset=15,
                        end_lineno=10,
                        end_col_offset=42,
                        elts=[
                            Constant(lineno=10, col_offset=16, end_lineno=10, end_col_offset=28, value='pad.common', kind=None),
                            Constant(lineno=10, col_offset=30, end_lineno=10, end_col_offset=41, value='note.note', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=12,
                    col_offset=4,
                    end_lineno=12,
                    end_col_offset=30,
                    targets=[Name(lineno=12, col_offset=4, end_lineno=12, end_col_offset=15, id='_pad_fields', ctx=Store())],
                    value=List(
                        lineno=12,
                        col_offset=18,
                        end_lineno=12,
                        end_col_offset=30,
                        elts=[Constant(lineno=12, col_offset=19, end_lineno=12, end_col_offset=29, value='note_pad', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    lineno=14,
                    col_offset=4,
                    end_lineno=14,
                    end_col_offset=79,
                    targets=[Name(lineno=14, col_offset=4, end_lineno=14, end_col_offset=16, id='note_pad_url', ctx=Store())],
                    value=Call(
                        lineno=14,
                        col_offset=19,
                        end_lineno=14,
                        end_col_offset=79,
                        func=Attribute(
                            lineno=14,
                            col_offset=19,
                            end_lineno=14,
                            end_col_offset=30,
                            value=Name(lineno=14, col_offset=19, end_lineno=14, end_col_offset=25, id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(lineno=14, col_offset=31, end_lineno=14, end_col_offset=40, value='Pad Url', kind=None)],
                        keywords=[
                            keyword(
                                lineno=14,
                                col_offset=42,
                                end_lineno=14,
                                end_col_offset=66,
                                arg='pad_content_field',
                                value=Constant(lineno=14, col_offset=60, end_lineno=14, end_col_offset=66, value='memo', kind=None),
                            ),
                            keyword(
                                lineno=14,
                                col_offset=68,
                                end_lineno=14,
                                end_col_offset=78,
                                arg='copy',
                                value=Constant(lineno=14, col_offset=73, end_lineno=14, end_col_offset=78, value=False, kind=None),
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