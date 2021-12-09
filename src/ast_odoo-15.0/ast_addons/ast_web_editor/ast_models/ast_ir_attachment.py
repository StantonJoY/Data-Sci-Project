Module(
    body=[
        ImportFrom(
            module='werkzeug.urls',
            names=[alias(name='url_quote', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='SUPPORTED_IMAGE_MIMETYPES', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='image/gif', kind=None),
                    Constant(value='image/jpe', kind=None),
                    Constant(value='image/jpeg', kind=None),
                    Constant(value='image/jpg', kind=None),
                    Constant(value='image/png', kind=None),
                    Constant(value='image/svg+xml', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='SUPPORTED_IMAGE_EXTENSIONS', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='.gif', kind=None),
                    Constant(value='.jpe', kind=None),
                    Constant(value='.jpeg', kind=None),
                    Constant(value='.jpg', kind=None),
                    Constant(value='.png', kind=None),
                    Constant(value='.svg', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='IrAttachment',
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
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.attachment', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='local_url', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Attachment URL', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_local_url', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='image_src', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_image_src', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='image_width', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_image_size', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='image_height', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_image_size', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='original_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.attachment', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Original (unoptimized, unresized) attachment', kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_local_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='attachment', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='attachment', ctx=Load()),
                                        attr='url',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='attachment', ctx=Load()),
                                                    attr='local_url',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='attachment', ctx=Load()),
                                                attr='url',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='attachment', ctx=Load()),
                                                    attr='local_url',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Constant(value='/web/image/%s?unique=%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='attachment', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='attachment', ctx=Load()),
                                                            attr='checksum',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_image_src',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='attachment', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='attachment', ctx=Load()),
                                            attr='mimetype',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[Name(id='SUPPORTED_IMAGE_MIMETYPES', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='attachment', ctx=Load()),
                                                    attr='image_src',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='attachment', ctx=Load()),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='url', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='attachment', ctx=Load()),
                                                    attr='image_src',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='attachment', ctx=Load()),
                                                attr='url',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='unique', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='attachment', ctx=Load()),
                                                    attr='checksum',
                                                    ctx=Load(),
                                                ),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=8, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='attachment', ctx=Load()),
                                                attr='url',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='separator', ctx=Store())],
                                                    value=IfExp(
                                                        test=Compare(
                                                            left=Constant(value='?', kind=None),
                                                            ops=[In()],
                                                            comparators=[
                                                                Attribute(
                                                                    value=Name(id='attachment', ctx=Load()),
                                                                    attr='url',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                        body=Constant(value='&', kind=None),
                                                        orelse=Constant(value='?', kind=None),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='attachment', ctx=Load()),
                                                            attr='image_src',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=BinOp(
                                                        left=Constant(value='%s%sunique=%s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='attachment', ctx=Load()),
                                                                    attr='url',
                                                                    ctx=Load(),
                                                                ),
                                                                Name(id='separator', ctx=Load()),
                                                                Name(id='unique', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='name', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='url_quote', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='attachment', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='attachment', ctx=Load()),
                                                            attr='image_src',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=BinOp(
                                                        left=Constant(value='/web/image/%s-%s/%s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='attachment', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                Name(id='unique', ctx=Load()),
                                                                Name(id='name', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='mimetype', kind=None),
                                Constant(value='url', kind=None),
                                Constant(value='name', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_image_size',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='attachment', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='image', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='base64_to_image',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='attachment', ctx=Load()),
                                                        attr='datas',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='attachment', ctx=Load()),
                                                    attr='image_width',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='image', ctx=Load()),
                                                attr='width',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='attachment', ctx=Load()),
                                                    attr='image_height',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='image', ctx=Load()),
                                                attr='height',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='attachment', ctx=Load()),
                                                            attr='image_width',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=0, kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='attachment', ctx=Load()),
                                                            attr='image_height',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=0, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='datas', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_media_info',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Return a dict with the values that we need on the media dialog.', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_read_format',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Constant(value='id', kind=None),
                                                Constant(value='name', kind=None),
                                                Constant(value='description', kind=None),
                                                Constant(value='mimetype', kind=None),
                                                Constant(value='checksum', kind=None),
                                                Constant(value='url', kind=None),
                                                Constant(value='type', kind=None),
                                                Constant(value='res_id', kind=None),
                                                Constant(value='res_model', kind=None),
                                                Constant(value='public', kind=None),
                                                Constant(value='access_token', kind=None),
                                                Constant(value='image_src', kind=None),
                                                Constant(value='image_width', kind=None),
                                                Constant(value='image_height', kind=None),
                                                Constant(value='original_id', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
